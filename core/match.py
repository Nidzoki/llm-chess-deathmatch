import chess
import random

class Match:
    def __init__(self, player_white, player_black):
        self.player_white = player_white
        self.player_black = player_black
        self.board = chess.Board()
        self.moves = []
        self.result = None

    def board_str(self):
        return str(self.board)

    def game_state(self):
        return self.board.fen()

    def is_move_legal(self, move):
        return move in self.board.legal_moves

    def play_move(self, move):
        self.board.push(move)
        self.games.append(move)
        return self.board.is_game_over()

    def test_play(self):
        current_player = self.player_white
        while not self.board.is_game_over(claim_draw=True):
            
            try:
                move = chess.Move.from_uci(current_player.get_move(self.board.fen(), "white" if current_player == self.player_white else "black"))
                
                if move is None or move not in self.board.legal_moves:
                    print("Move is not legal. Making a random legal move instead.")
                    move = random.choice(list(self.board.legal_moves))
                    self.board.push(move)
                    print(f"{current_player.name} plays: {move.uci()}\n{self.board_str()}\n")
                else:
                    self.board.push(move)
                    print(f"{current_player.name} plays: {move.uci()}\n{self.board_str()}\n")
            except ValueError:
                print("Invalid move. Making a random legal move instead.")
                move = random.choice(list(self.board.legal_moves))
                self.board.push(move)
                print(f"{current_player.name} plays: {move.uci()}\n{self.board_str()}\n")

            current_player = self.player_black if current_player == self.player_white else self.player_white
        self.result = self.board.result()
