import pygame
from pygame.font import Font

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.pieces = []

    def move_piece(self, direction: str):
        # TODO: Implement piece movement logic based on the given direction
        pass

    def get_grid(self):
        return self.grid

    def get_pieces(self):
        return self.pieces

class Score:
    def __init__(self, value: int = 0):
        self.value = value

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value

class Level:
    def __init__(self, difficulty: int, max_value: int):
        self.difficulty = difficulty
        self.max_value = max_value

    def get_difficulty(self):
        return self.difficulty

    def get_max_value(self):
        return self.max_value

class UI:
    def __init__(self, theme: str, font: Font):
        self.theme = theme
        self.font = font

    def get_theme(self):
        return self.theme

    def get_font(self):
        return self.font

class Game:
    def __init__(self, board: Board, score: Score, level: Level, ui: UI):
        self.board = board
        self.score = score
        self.level = level
        self.ui = ui

    def play(self):
        # TODO: Implement game logic and main loop
        pass

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level

    def get_ui(self):
        return self.ui
