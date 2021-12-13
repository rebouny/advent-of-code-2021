#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import List, Tuple
import pprint


"""Basic algorithm:
1. increase level
2. get list of flashed tuples
3. for each flashed tupel increase value
4. do 3 while there are flashed tuples
5. get all tuples > 9 as highlights an reset them to zero
6. sum up all highlights
"""

def increase_level(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            grid[y][x] += 1

def get_flashes(grid):
    flashes = set()
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if (grid[y][x] > 9):
                flashes.add((y, x))
    return flashes

def fire_neighbors(grid, y, x):
    """Calculates min and max index of each coordinates. Examples are
    0/0 y:0-1 x:0-1
    0/9 y:0-1 x:8-9
    0/5 y:0-1 x:4-6
    5/0 y:4-6 x:0-1
    9/9 x:8-9 x:8-9
    """
    y_min = y-1 if y > 0 else y
    y_max = y+1 if y < len(grid) - 1 else y
    x_min = x-1 if x > 0 else x
    x_max = x+1 if x < len(grid[y]) - 1 else x
    
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            grid[y][x] += 1


def flash(grid, flashes: List[Tuple[int, int]]):
    for (y, x)  in flashes:
        fire_neighbors(grid, y, x)
        

def reset_and_count(grid) -> int:
    count = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if (grid[y][x] > 9):
                count += 1
                grid[y][x] = 0
    return count


def read_grid(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    grid = list()
    for line in lines:
        grid.append([int(x) for x in line])
    return grid

#def chunks(lst, n):
#    """Debugging helper: yield successive n-sized chunks from lst."""
#    for i in range(0, len(lst), n):
#        yield lst[i:i + n]

def solve(filename: str, n: int) -> None:
    grid = read_grid(filename)
    count = 0

    iteration = 1
    while True:
        increase_level(grid)
        fired = set()
        while True:
            flashes = get_flashes(grid)
            to_fire = flashes.difference(fired)
            
            if len(to_fire) == 0:
                break
            flash(grid, to_fire)
            fired = fired.union(to_fire)

        count += reset_and_count(grid)

        if iteration == n:
            break
        if (n == -1) and (len(fired) == len(grid) * len(grid[0])):
            break
        iteration += 1

    print(f"ended at iteration {iteration} with sum {count}")
    #pprint.pprint(list(chunks(grid, len(grid[0]))))


def part_1(filename: str) -> None:
    solve(filename, 195)

def part_2(filename: str) -> None:
    solve(filename, -1)


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)