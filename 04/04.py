#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


"""solution uses a one dimensional data structure.
   we keep track of horizontal and vertical layout
   by storing the necessary positions to check.
"""
indexes = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24]
]


class Board:
    def __init__(self, numbers):
        """one dimensional array of tuples (number, is_striked_out)"""
        self.items = [ (n, False) for n in numbers]
        self.has_won = False

    def _eval_winning_condition(self) -> None:
        for i in indexes:
            if (all(self.items[x][1] == True for x in i)):
                self.has_won = True
                return

    def calc_score(self, winner) -> int:
        return winner * sum([x[0] if x[1] == False else 0 for x in self.items])

    def strikeout(self, number) -> None:
        """"marks given number and evaluates winning condition"""
        for idx, x in enumerate(self.items):
            if x[0] == number:
                self.items[idx] = (number, True)

        self._eval_winning_condition()

    def wins(self) -> bool:
        return self.has_won

    @staticmethod
    def open_boards(boards) -> int:
        """"""
        return sum([0 if b.wins() else 1 for b in boards])

    def __str__(self) -> str:
        return " ".join(f"({i[0]}/{i[1]})" for i in self.items)


def init_board_from_input(lines):
    return [int(x) for x in " ".join(lines).split() if x.isdigit()]

def read_input(filename: str):
    with open(filename, "r") as f:
        numbers = [int(x) for x in f.readline().rstrip().split(",")]

        # split and filter empty lines
        lines = list(filter(None, f.read().splitlines()))

    boards = [ Board(init_board_from_input(lines[i:i+5]) ) for i in range(0, len(lines), 5)  ]
    
    return numbers, boards


def part_1(filename: str) -> None:
    numbers, boards = read_input(filename)

    for number in numbers:
        for idx, board in enumerate(boards):

            board.strikeout(number)

            if board.wins():
                score = board.calc_score(number)
                print(f"{idx+1} wins with {score} points")
                return


def part_2(filename: str) -> None:
    numbers, boards = read_input(filename)

    for number in numbers:
        for idx, board in enumerate(boards):
            if board.wins():
                continue

            board.strikeout(number)

            if board.wins() and Board.open_boards(boards) == 0:
                score = board.calc_score(number)
                print(f"{idx+1} wins with {score} points")
                return

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)