#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
from typing import List, Tuple

REGEX = re.compile(r'.*\ (x|y)=(\d+)')


class Grid(object):
    def __init__(self, data) -> None:
        max_y, max_x = self._find_max(data)
        self.g = []

        for _ in range(max_y + 1):
            self.g.append([0] * (max_x + 1))
        for x, y in data:
            self.g[y][x] = 1

            
    def _find_max(self, data) -> Tuple[int, int]:
        max_y = max(data, key=lambda x: x[1])[1]
        max_x = max(data, key=lambda x: x[0])[0]

        return max_y, max_x

    def fold(self, coord, pos) -> None:
        if coord == "y":
            self.g =[ [1 if x>0 or y>0 else 0 for x, y in zip(self.g[y], self.g[-(y+1)])] for y in range(pos)]
        else:
            self.g = [ [ 1 if y[x]>0 or y[-(x+1)]>0 else 0 for x in range(pos)] for y in self.g ]

    def sum_dots(self) -> int:
        return sum(sum(self.g[i]) for i in range(len(self.g)))

    def get_grid(self) -> List[List[int]]:
        return self.g


def read_data(filename: str) -> Tuple[List[Tuple[int,int]],List[Tuple[str,int]]]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    data = []
    instructions = []

    idx = lines.index("")

    for line in lines[0:idx]:
        a, b = line.split(",", 2)
        data.append((int(a), int(b)))   
    for line in lines[idx+1:]:
        if (m := re.match(REGEX, line)):
            coord = m.group(1)
            n = m.group(2)
            instructions.append((coord, int(n)))     

    return data, instructions


def part_1(filename: str) -> None:
    data, instructions = read_data(filename)

    g = Grid(data)

    i = instructions[0]
    g.fold(i[0], i[1])

    print (g.sum_dots())


def part_2(filename: str) -> None:
    data, instructions = read_data(filename)

    g = Grid(data)

    for i in instructions:
        g.fold(i[0], i[1])

    for y in g.get_grid():
        print("".join(['#' if x >0 else " " for x in y]))
    

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)