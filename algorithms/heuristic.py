from reversi.board import points, possible_moves
from reversi.board import PLAYER_1_WHITE, PLAYER_2_BLACK

EARLY_GAME_DISKS = 16
END_GAME_DISKS = 36
MULTIPLIER = 100
CELL_WEIGHTS: list[list[int]] = [
    [4, -3, 2, 2, 2, 2, -3, 4],
    [-3, -4, -1, -1, -1, -1, -4, -3],
    [2, -1, 1, 0, 0, 1, -1, 2],
    [2, -1, 0, 1, 1, 0, -1, 2],
    [2, -1, 0, 1, 1, 0, -1, 2],
    [2, -1, 1, 0, 0, 1, -1, 2],
    [-3, -4, -1, -1, -1, -1, -4, -3],
    [4, -3, 2, 2, 2, 2, -3, 4]
]


def coin_parity(board: list[list[int]]) -> (int, int):
    p1_heurestic_points, p2_heurestic_points = points(board)
    max_player_coins = max(p1_heurestic_points, p2_heurestic_points)
    min_player_coins = min(p1_heurestic_points, p2_heurestic_points)
    coin_parity = int(MULTIPLIER * (max_player_coins - min_player_coins) / (max_player_coins + min_player_coins))

    if p1_heurestic_points > p2_heurestic_points:
        return coin_parity, -coin_parity
    elif p1_heurestic_points < p2_heurestic_points:
        return -coin_parity, coin_parity
    else:
        return 0, 0


def mobility(board: list[list[int]]) -> (int, int):
    p1_mobility = len(possible_moves(board, PLAYER_1_WHITE))
    p2_mobility = len(possible_moves(board, PLAYER_2_BLACK))

    max_actual_moves = max(p1_mobility, p2_mobility)
    min_actual_moves = min(p1_mobility, p2_mobility)
    heurestic_value = int(MULTIPLIER * (max_actual_moves - min_actual_moves) / (max_actual_moves + min_actual_moves))
    if p1_mobility > p2_mobility:
        return heurestic_value, -heurestic_value
    elif p1_mobility < p2_mobility:
        return -heurestic_value, heurestic_value
    else:
        return 0, 0


def weights(board: list[list[int]]) -> (int, int):
    p1_heurestic_points, p2_heurestic_points = 0, 0
    for row_number, row in enumerate(board):
        for column_number, cell in enumerate(row):
            if cell == PLAYER_1_WHITE:
                p1_heurestic_points += CELL_WEIGHTS[row_number][column_number]
            if cell == PLAYER_2_BLACK:
                p2_heurestic_points += CELL_WEIGHTS[row_number][column_number]
    return p1_heurestic_points, p2_heurestic_points


def adjustable_heurestic(board: list[list[int]], player: int):
    p1_disks, p2_disks = points(board)
    disks_on_board = p1_disks + p2_disks
    
    if disks_on_board < EARLY_GAME_DISKS:
        p1_heurestic_points, p2_heurestic_points = coin_parity(board)
    elif EARLY_GAME_DISKS <= disks_on_board < EARLY_GAME_DISKS:
        p1_heurestic_points, p2_heurestic_points = mobility(board)
    else:
        p1_heurestic_points, p2_heurestic_points = weights(board)

    if player == PLAYER_1_WHITE:
        return p1_heurestic_points - p2_heurestic_points
    else:
        return p2_heurestic_points - p1_heurestic_points
