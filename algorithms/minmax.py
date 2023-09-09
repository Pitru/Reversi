import math

from reversi.board import is_game_ended, points, reverse_player, possible_moves, do_move
from algorithms.heuristic import adjustable_heurestic


def minmax(player: int, board: dict[int, dict[int, int]], depth: int, maximizing: bool):
    moves: dict[(int, int): list[(int, int)]] = possible_moves(board, player)
    if is_game_ended(board):
        p1, p2 = points(board)
        if player == 1:
            return p1-p2
        else:
            return p2-p1
    if depth == 0:
        return adjustable_heurestic(board, player)
    if not moves:
        if player == 1:
            return -100
        else:
            return 100

    if maximizing:
        value = -math.inf
        for cell, cells in moves.items():
            new_board = do_move(board, cell, player, cells)
            value = max(value, minmax(reverse_player(player), new_board, depth-1, not maximizing))
        return value
    else:
        value = math.inf
        for cell, cells in moves.items():
            new_board = do_move(board, cell, player, cells)
            value = min(value, minmax(reverse_player(player), new_board, depth-1, not maximizing))
        return value


def minmax_start(player: int, board: dict[int, dict[int, int]], depth: int) -> (int, int):
    best_move = ()
    best_score = -math.inf
    for cell in possible_moves(board, player).keys():
        score = minmax(player, board, depth, False)
        if score > best_score:
            best_move = cell
            best_score = score
    return best_move
