import math
from reversi.board import is_game_ended, points, reverse_player, possible_moves, do_move, PLAYER_1_WHITE
from algorithms.heuristic import adjustable_heurestic


def alpha_beta_pruning(player: int, board: list[list[int]], depth: int, alpha: float = -math.inf, beta: float = math.inf, maximizing: bool = True) -> int:
    moves: dict[(int, int): list[(int, int)]] = possible_moves(board, player)

    if is_game_ended(board):
        p1_points, p2_points = points(board)
        if player == PLAYER_1_WHITE:
            return p1_points - p2_points
        else:
            return p2_points - p1_points
    if depth == 0:
        return adjustable_heurestic(board, player)
    if not moves:
        if player == PLAYER_1_WHITE:
            return -100
        else:
            return 100

    if maximizing:
        value = -math.inf
        for move, affected_cells in moves.items():
            new_board = do_move(board, move, player, affected_cells)
            value = max(value, alpha_beta_pruning(reverse_player(player), new_board, depth-1, alpha, beta, not maximizing))
            alpha = max(alpha, value)
            if alpha >= beta:
                return alpha  
        return value
    else:
        value = math.inf
        for move, affected_cells in moves.items():
            new_board = do_move(board, move, player, affected_cells)
            value = min(value, alpha_beta_pruning(reverse_player(player), new_board, depth-1, alpha, beta, not maximizing))
            beta = min(beta, value)
            if alpha >= beta:
                return beta
        return value
        

def alpha_beta_pruning_start(player: int, board: list[list[int]], max_depth: int) -> (int, int):
    best_move = ()
    best_score = -math.inf
    for cell in possible_moves(board, player).keys():
        score = alpha_beta_pruning(player, board, max_depth)
        if score > best_score:
            best_move = cell
            best_score = score
    return best_move
