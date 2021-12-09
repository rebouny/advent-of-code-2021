#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
from typing import List, Set

def read_grid(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    width = len(lines[0])

    grid = list()
    grid.append([10] * (width + 2))
    for line in lines:
        grid.append([10, *[int(x) for x in line], 10])
    grid.append([10] * (width + 2))
    
    return grid


def check_neighbors(value: int, *elements: List[int]):
    return all([value < element for element in elements])


def check_coords(g:List[List[int]], coords: Set[int], j: int, i: int) -> int:
    if g[j][i] > 8 or (j, i) in coords:
        return 0

    coords.add((j, i))
    return 1 + check_coords(g, coords, j-1, i) + check_coords(g, coords, j+1, i) + check_coords(g, coords, j, i-1) + check_coords(g, coords, j, i+1)


def get_low_points(g: List[List[int]]) -> Set[int]:
    width = len(g[0]) - 2
    height = len(g) - 2

    low_points = set()

    for j in range(1, height + 1):
        for i in range(1, width + 1):
            if (check_neighbors(g[j][i], g[j-1][i], g[j+1][i],g[j][i-1], g[j][i+1])):
                low_points.add((j, i))
    return low_points

def part_1(filename: str) -> None:
    g = read_grid(filename)

    low_points = get_low_points(g)

    sum_risk = 0 
    for j, i in low_points:
        sum_risk += g[j][i] + 1
    print(sum_risk)
            

def part_2(filename: str) -> None:
    g = read_grid(filename)

    low_points = get_low_points(g)
    basin_sizes = list()

    for j, i in low_points:
        basin_sizes.append(check_coords(g, set(), j, i))

    basin_sizes.sort(reverse=True)
    print(math.prod(basin_sizes[0:3]))
    

if __name__ == "__main__":
    filename = sys.argv[1]

    #part_1(filename)
    part_2(filename)