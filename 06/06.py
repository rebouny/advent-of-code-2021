#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def read_input(filename: str):
    with open(filename, "r") as f:
        state = [int(x) for x in f.readline().rstrip().split(",")]

    return state


def solution(filename: str, days: int) -> None:
    data = read_input(filename)

    state = { x: data.count(x) for x in data }
    
    for i in range (days):
        state = { k - 1: v for k, v in state.items()}

        spawning = state.pop(-1, None)

        if spawning:
            # add "births" and reset "parents" 
            state[8] = spawning
            state[6] = state.get(6,0) + spawning
        
        #print(f"After {i+1:3d} day{': ' if i == 0 else 's:'} {state}")
        
    print(sum([state[k] for (k,_) in state.items()]))


def part_1(filename: str) -> None:
    solution(filename, 80)


def part_2(filename: str) -> None:
    solution(filename, 256)


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)
