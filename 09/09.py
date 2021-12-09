#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
from typing import List, Set


def read_grid(filename: str) -> List[List[int]]:
    """Initializes grid from file input. As we only read values from 0 to 9 it
    is allow wrap a border of 10s around our grid to avoid boundary index
    checks. Returns a 2d grid then of integer values that is a bit larger than
    our input ;)
    """
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    width = len(lines[0])

    grid = list()
    grid.append([10] * (width + 2))
    grid.extend([10, *[int(x) for x in line], 10] for line in lines)
    grid.append([10] * (width + 2))
    
    return grid


def is_low(g: List[List[int]], j: int, i: int) -> bool:
    """Queries neighborhood to find out if point is 'low'"""
    return all(g[j][i] < n for n in [ g[j-1][i], g[j+1][i], g[j][i-1], g[j][i+1] ])


def region(g:List[List[int]], coords: Set[int], j: int, i: int) -> int:
    """Recursion that traverses each neighborhood node that hasn't been
    recorded yet and satisfied the criteria to belong to a region
    """
    if g[j][i] > 8 or (j, i) in coords:
        return 0

    coords.add((j, i))
    return 1 + region(g, coords, j-1, i) + region(g, coords, j+1, i) + region(g, coords, j, i-1) + region(g, coords, j, i+1)


def get_low_points(g: List[List[int]]) -> Set[int]:
    width = len(g[0]) - 2
    height = len(g) - 2

    return set([ (j, i) for i in range(1, width + 1) for j in range(1, height + 1) if is_low(g, j, i) ])
   
   
def part_1(filename: str) -> None:
    g = read_grid(filename)

    low_points = get_low_points(g)

    # accumulated 'height's of basins
    print(sum([(g[j][i] + 1) for j, i in low_points]))
            

def part_2(filename: str) -> None:
    g = read_grid(filename)
    
    low_points = get_low_points(g)
    
    # top 3 of biggest regions
    print(math.prod(sorted([region(g, set(), j, i) for j, i in low_points])[-3:]))

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)