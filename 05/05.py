#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import UnsupportedOperation
import sys
import re
from collections.abc import Iterator
import pprint

REGEX = re.compile(r'(\d+),(\d+)\ \-> (\d+),(\d+)\s*')

def chunks(lst, n):
    """Debugging helper: yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class Board(object):
    """Main playground, stores data in one-dimenaional array beside dimensions.
       Items of the board consist of a counter how many lines intersect with an item"""
    def __init__(self, width: int, height: int):
        self.items = [ 0 for _ in range(width * height)]
        self.width = width
        self.height = height

    def inc(self, x: int, y: int):
        try:
            self.items[ y * self.width + x] += 1
        except IndexError as e:
            print(x, y)
            raise e

    def sum_overlaps(self, gte: int):
        return sum([1 if i >= gte else 0 for i in self.items])

    def dump(self) -> None:
        """Debugging helper used during development"""
        pprint.pprint(list(chunks(self.items, self.width)))


class LineIterator(Iterator):
    """Creates an iterator for line element travesal.
       This will probably totally suxxs when using diagonal lines..."""
    def __init__(self, line):
        self.line = line
        self.current = line.start
        self.stop_iteration = False
        self.dir_x = 0
        self.dir_y = 0
        if line.start[0] < line.end[0]:
            self.dir_x = 1
        elif line.start[0] > line.end[0]:
            self.dir_x = -1
        if line.start[1] < line.end[1]:
            self.dir_y = 1
        elif line.start[1] > line.end[1]:
            self.dir_y = -1
        

    def __next__(self):
        if self.stop_iteration:
            raise StopIteration

        retval = self.current

        if (self.current == self.line.end):
            self.stop_iteration = True

        self.current = (self.current[0] + self.dir_x, self.current[1] + self.dir_y)
        
        return retval


class Line(object):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.start = (x1, y1)
        self.end = (x2, y2)

    def is_diagonal(self) -> bool:
        return not self.is_horizontal() and not self.is_vertical()

    def is_horizontal(self) -> bool:
        return self.start[0] == self.end[0]

    def is_vertical(self) -> bool:
        return self.start[1] == self.end[1]

    def __str__(self) -> str:
        return f"{self.start[0]},{self.start[1]} -> {self.end[0]},{self.end[1]}" \
               f" {self.is_horizontal()} {self.is_vertical()} {self.is_diagonal()}"

    @staticmethod
    def get_dimension(lines):
        idx_width = max(max(lines, key=lambda x: x.start[0]).start[0],
                    max(lines, key=lambda x: x.end[0]).end[0])
        idx_height = max(max(lines, key=lambda x: x.start[1]).start[1],
                    max(lines, key=lambda x: x.end[1]).end[1])

        # you know, this value and index thing and the off-by-one errors...
        return idx_width + 1, idx_height + 1
        
    @staticmethod
    def filter_diagonal(lines):
        return filter(lambda x: x.is_diagonal(), lines)
        

def read_input(filename: str) -> list:
    lines = list()
    with open(filename, "r") as f:
        for line in f:
            if (m := re.match(REGEX, line)):
                x1 = int(m.group(1))
                y1 = int(m.group(2))
                x2 = int(m.group(3))
                y2 = int(m.group(4))
                lines.append(Line(x1, y1, x2, y2))
    return lines

def part_1(filename: str) -> None:
    lines = read_input(filename)

    width, height = Line.get_dimension(lines)
    
    # drop out diagonal lines
    diagonals = list(Line.filter_diagonal(lines))
    not_diagonals = list(set(lines) - set(diagonals))
    
    board = Board(width, height)

    for line in not_diagonals:
        for i in LineIterator(line):
            board.inc(i[0], i[1])

    print(Board.sum_overlaps(board, 2))

    #board.dump()

def part_2(filename: str) -> None:
    lines = read_input(filename)

    width, height = Line.get_dimension(lines)
    
    board = Board(width, height)

    for line in lines:
        for i in LineIterator(line):
            board.inc(i[0], i[1])

    print(Board.sum_overlaps(board, 2))

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)