from copy import deepcopy
from io import StringIO

BOARD_SIZE = 8
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
TOP_ROW = "  A B C D E F G H \n"
WHITE_PLAYER_DISK = "■"
BLACK_PLAYER_DISK = "□"
EMPTY_DISK = "🞅"

PLAYER_1_WHITE = 1
PLAYER_2_BLACK = 2
EMPTY_CELL = 0
MAPPING  = {EMPTY_CELL: EMPTY_DISK, PLAYER_1_WHITE: WHITE_PLAYER_DISK, PLAYER_2_BLACK: BLACK_PLAYER_DISK}


def empty_cells_number(board: list[list[int]]) -> int:
    flatten_board = [cell for row in board for cell in row]
    number_of_empty_cells = flatten_board.count(EMPTY_CELL)
    return number_of_empty_cells


def generate_empty_board() -> list[list[int]]:
    board = []
    for a in range(8):
        row = []
        for b in range(8):
            row.append(EMPTY_CELL)
        board.append(row)
    return board


def generate_start_board() -> list[list[int]]:
    board = generate_empty_board()
    board[3][3] = PLAYER_2_BLACK
    board[4][4] = PLAYER_2_BLACK
    board[4][3] = PLAYER_1_WHITE
    board[3][4] = PLAYER_1_WHITE
    return board


def print_board(board: list[list[int]]) -> None:
    string_buider = StringIO()
    string_buider.write(TOP_ROW)
    for row_number, row in enumerate(board):
        string_buider.write(str(row_number + 1) + " ")
        for cell in row:
            string_buider.write(MAPPING[cell] + " ")
        string_buider.write("\n")
    print(string_buider.getvalue())


def is_cell_on_board(cell_coords: (int, int)) -> bool:
    x, y = cell_coords
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE


def is_board_full(board: list[list[int]]) -> bool:
    for row in board:
        for cell in row:
            if cell == EMPTY_CELL:
                return False
    return True


def is_game_ended(board: list[list[int]]) -> bool:
    player_1_points, player_2_points = points(board)
    player_1_moves = possible_moves(board, PLAYER_1_WHITE)
    player_2_moves = possible_moves(board, PLAYER_2_BLACK)
    return is_board_full(board) or (not player_1_moves and not player_2_moves) or player_1_points == 0 or player_2_points == 0


def points(board: list[list[int]]) -> (int, int):
    flatten_board = [cell for row in board for cell in row]
    player_1_points = flatten_board.count(PLAYER_1_WHITE)
    player_2_points = flatten_board.count(PLAYER_2_BLACK)
    return player_1_points, player_2_points


def reverse_player(player: int):
    if player == PLAYER_1_WHITE:
        return PLAYER_2_BLACK
    if player == PLAYER_2_BLACK:
        return PLAYER_1_WHITE


def possible_moves(board: list[list[int]], player: int) -> dict[(int, int): list[(int, int)]]:
    possible_moves = {}
    for row_number, row in enumerate(board):
        for column_number, cell in enumerate(row):
            if cell == EMPTY_CELL:
                move = (row_number, column_number)
                cells_to_change = cells_to_change_by_move(board, player, move)
                if cells_to_change:
                    possible_moves[(row_number, column_number)] = cells_to_change
    return possible_moves


def cells_to_change_by_move(board: list[list[int]], player: int, cell: (int, int)) -> list[(int, int)]:
    enemy_player = reverse_player(player)
    x, y = cell
    cells_to_change = []
    for direction in DIRECTIONS:
        searched_row = x + direction[0]
        searched_column = y + direction[1]
        if is_cell_on_board((searched_row, searched_column)) and board[searched_row][searched_column] == enemy_player:
            cells_to_change_in_scope = []
            while is_cell_on_board((searched_row, searched_column)) and board[searched_row][searched_column] != 0:
                if board[searched_row][searched_column] == enemy_player:
                    cells_to_change_in_scope.append((searched_row, searched_column))
                if board[searched_row][searched_column] == player:
                    cells_to_change = cells_to_change + cells_to_change_in_scope
                    break
                searched_row += direction[0]
                searched_column += direction[1]
    return cells_to_change


def do_move(board: list[list[int]], move: (int, int), player: int, affected_cells: list[(int, int)]) -> dict:
    x, y = move
    if not is_cell_on_board(move):
        raise Exception("Cell is not on board")
    if board[x][y] != EMPTY_CELL:
        raise Exception("Cell is not empty")

    new_board = deepcopy(board)
    
    for cell in affected_cells:
        r, c = cell
        new_board[r][c] = player
    new_board[x][y] = player
    return new_board


def move_to_string(move: (int, int)) -> str:
    row, col = move
    return chr(col + 65) + str(row + 1)