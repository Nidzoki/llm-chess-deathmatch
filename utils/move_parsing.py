import chess

def parse_and_validate_move(board, move_uci):
    """
    Parses a move in UCI format and validates if it is a legal move.
    Returns the move object if it is valid, otherwise returns None.
    """
    try:
        candidate_move = chess.Move.from_uci(move_uci)
        if candidate_move in board.legal_moves:
            return candidate_move
    except (ValueError, TypeError):
        return None
    return None
