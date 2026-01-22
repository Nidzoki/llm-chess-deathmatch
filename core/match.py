import chess
import chess.pgn
import random
import datetime
import json
import re
import os

class Match:
    def __init__(self, player_white, player_black):
        self.player_white = player_white
        self.player_black = player_black
        self.board = chess.Board()
        self.game = chess.pgn.Game()
        self.moves = []
        self.result = None

        self.game.headers["Event"] = "AI Chess Match"
        self.game.headers["White"] = player_white.name
        self.game.headers["Black"] = player_black.name
        self.game.headers["Date"] = datetime.datetime.now().strftime("%Y.%m.%d")

        # Sanitize player names for filename and add a timestamp
        white_name = re.sub(r'[^\w\-.]', '_', player_white.name)
        black_name = re.sub(r'[^\w\-.]', '_', player_black.name)
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.illegal_move_log_file = f"gamedata/logs/{white_name}_vs_{black_name}_{timestamp}_illegal_moves.log"
        self.pgn_filename = f"gamedata/pgns/{white_name}_vs_{black_name}_{timestamp}.pgn"

    def _log_illegal_move(self, player_name, opponent_name, board_fen, attempted_move, move_number):
        os.makedirs(os.path.dirname(self.illegal_move_log_file), exist_ok=True)
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "player": player_name,
            "opponent": opponent_name,
            "move_number": move_number,
            "board_fen": board_fen,
            "attempted_move_uci": str(attempted_move) if attempted_move is not None else None
        }
        with open(self.illegal_move_log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def board_str(self):
        return str(self.board)

    def game_state(self):
        return self.board.fen()

    def is_move_legal(self, move):
        return move in self.board.legal_moves

    def play_move(self, move):
        self.board.push(move)
        self.moves.append(move)
        self.game = self.game.add_variation(move)
        
        return self.board.is_game_over()

    def test_play(self):
        current_player = self.player_white
        node = self.game
        while not self.board.is_game_over(claim_draw=True):
            board_fen = self.board.fen()
            move = None
            move_uci = None
            
            try:
                move_uci = current_player.get_move(board_fen, "white" if current_player == self.player_white else "black")
                candidate_move = chess.Move.from_uci(move_uci)
                if candidate_move in self.board.legal_moves:
                    move = candidate_move
            except (ValueError, TypeError):
                pass

            if move is None:
                move_number = self.board.ply() // 2 + 1
                opponent_name = self.player_black.name if current_player == self.player_white else self.player_white.name
                self._log_illegal_move(current_player.name, opponent_name, board_fen, move_uci, move_number)
                print("AI returned invalid/illegal move. Making a random legal move instead.")
                move = random.choice(list(self.board.legal_moves))

            self.board.push(move)
            node = node.add_variation(move)
            print(f"{current_player.name} plays: {move.uci()}\n{self.board_str()}\n")

            current_player = self.player_black if current_player == self.player_white else self.player_white
        self.result = self.board.result()
        os.makedirs(os.path.dirname(self.pgn_filename), exist_ok=True)
        with open(self.pgn_filename, "w") as pgn_file:
            print(self.game, file=pgn_file, end="\n\n")

    def play_with_user(self):
        current_player = self.player_white
        node = self.game

        while not self.board.is_game_over(claim_draw=True):
            player_color_str = "white" if current_player == self.player_white else "black"
            move = None

            # Simple check if the current player is human, by checking if 'get_move' is missing
            if not hasattr(current_player, 'get_move'):
                valid_input = False
                while not valid_input:
                    try:
                        move_uci = input(f"Enter your move for {player_color_str} (in UCI format, e.g. e2e4): ")
                        move = chess.Move.from_uci(move_uci)
                        if move in self.board.legal_moves:
                            valid_input = True
                        else:
                            print("Illegal move. Try again.")
                    except ValueError:
                        print("Invalid UCI format. Try again.")
            else: # AI player
                board_fen = self.board.fen()
                move_uci = None
                try:
                    move_uci = current_player.get_move(board_fen, player_color_str)
                    candidate_move = chess.Move.from_uci(move_uci)
                    if candidate_move in self.board.legal_moves:
                        move = candidate_move
                except (ValueError, IndexError, TypeError):
                    pass
                
                if move is None:
                    move_number = self.board.ply() // 2 + 1
                    opponent_name = self.player_black.name if current_player == self.player_white else self.player_white.name
                    self._log_illegal_move(current_player.name, opponent_name, board_fen, move_uci, move_number)
                    print("AI returned invalid/illegal move. Making a random legal move instead.")
                    move = random.choice(list(self.board.legal_moves))
            
            self.board.push(move)
            node = node.add_variation(move)
            print(f"{current_player.name} plays: {move.uci()}\n{self.board_str()}\n")

            current_player = self.player_black if current_player == self.player_white else self.player_white
        
        self.result = self.board.result()
        print(f"Game over. Result: {self.result}")
        user_pgn_filename = self.pgn_filename.replace(".pgn", "_with_user.pgn")
        os.makedirs(os.path.dirname(user_pgn_filename), exist_ok=True)
        # Save to a different file to not overwrite test_play results
        with open(user_pgn_filename, "w") as pgn_file:
            print(self.game, file=pgn_file, end="\n\n")
