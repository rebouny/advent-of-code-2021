#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools
import re


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
        self.items = [ (n, False) for n in numbers]

    def wins(self) -> bool:
        for i in indexes:
            if (all(self.items[x][1] == True for x in i)):
                return True

        return False

    def calc_score(self, winner) -> int:
        return winner * sum([x[0] if x[1] == False else 0 for x in self.items])

    def strikeout(self, number) -> None:
        for idx, x in enumerate(self.items):
            if x[0] == number:
                self.items[idx] = (number, True)

    def __str__(self):
        return " ".join(f"({i[0]}/{i[1]})" for i in self.items)


def read_input(filename: str):
    numbers = list()
    boards = list()

    with open(filename, "r") as f:
        numbers = [int(x) for x in f.readline().rstrip().split(",")]

        # split and filter empty lines
        lines = list(filter(None, f.read().splitlines()))

    for i in range(0, len(lines), 5):
        b = [int(x) for x in " ".join(lines[i:i+5]).split() if x.isdigit()]
        board = Board(b)
        boards.append(board)

    return numbers, boards


def part_1(filename: str) -> None:
    numbers, boards = read_input(filename)

    # main loop over every input
    for number in numbers:
        for board in boards:
            board.strikeout(number)
            if board.wins():
                score = board.calc_score(number)
                print(f"{number+1} wins with {score} points")
                return

def part_2(filename: str) -> None:
    pass

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)