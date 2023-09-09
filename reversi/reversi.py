from reversi.board import generate_start_board, is_game_ended, do_move, possible_moves, points, print_board, move_to_string, PLAYER_1_WHITE, PLAYER_2_BLACK
from reversi.players import MinmaxPlayer, AlphabetaPlayer


class Reversi:
    def __init__(self):
        self.player_1 = AlphabetaPlayer(PLAYER_1_WHITE)
        self.player_2 = MinmaxPlayer(PLAYER_2_BLACK)
        self.active_player = self.player_2
        self.board = generate_start_board()

    def start_game(self):
        while not is_game_ended(self.board):
            print(f"{'BLACK' if self.active_player.player_number == 2 else 'WHITE'} player turn:")
            print_board(self.board)
            
            move = self.active_player.move(self.board)
            moves_and_cells_to_change = possible_moves(self.board, self.active_player.player_number)
            cells = moves_and_cells_to_change[move]
            self.board = do_move(self.board, move, self.active_player.player_number, cells)
            
            print(f"Player: {'BLACK' if self.active_player.player_number == 2 else 'WHITE'} moved: {move_to_string(move)}\n\n")
            
            enemy_player = self.ememy_player()
            if possible_moves(self.board, enemy_player.player_number):
                self.active_player = enemy_player
                
        print("Game ended")
        print_board(self.board)
        player1_points, player2_points = points(self.board)
        if player2_points > player1_points:
            print(f"BLACK player won:\n {player2_points} to {player1_points}")
        if player1_points > player2_points:
            print(f"WHITe player won:\n {player1_points} to {player2_points}")


    def ememy_player(self):
        if self.active_player == self.player_1:
            return self.player_2
        else:
            return self.player_1
