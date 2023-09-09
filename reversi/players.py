import re
import time
from abc import ABC, abstractmethod
from os import environ

from algorithms.minmax import minmax_start
from algorithms.alfabeta import alpha_beta_pruning_start

DEPTH = int(environ.get("DEPTH", 3))

def execution_time(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, *kwargs)
        print(f"Time: {time.perf_counter()-start_time:.3f}s")
        return result
    return inner


class HumanPlayer(ABC):
    def __init__(self, player_number: int):
        self.player_number = player_number

    def move(self, board):
        move = input("Your move:\t")
        while not re.search(r"^[a-hA-H][1-8]$|^[1-8][a-hA-H]$", move):
            print("Invalid move. Try again.")
            move = input("Your move:\t")    
        col = self.mapping[re.findall(r'[a-hA-H]', move)[0].lower()]
        row = int(re.findall(r'[1-8]', move)[0]) - 1
        return row, col
    
    
class AbstractPlayer(ABC):
    def __init__(self, player_number: int):
        self.player_number = player_number

    @abstractmethod
    def move(self, board):
        raise NotImplementedError


class MinmaxPlayer(AbstractPlayer):
    def __init__(self, player_number: int):
        super().__init__(player_number)

    @execution_time
    def move(self, board):
        move = minmax_start(self.player_number, board, DEPTH)
        return move


class AlphabetaPlayer(AbstractPlayer):
    def __init__(self, player_number: int):
        super().__init__(player_number)

    @execution_time
    def move(self, board):
        move = alpha_beta_pruning_start(self.player_number, board, DEPTH)
        return move
