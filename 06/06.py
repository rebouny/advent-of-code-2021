#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
    

def read_input(filename: str):
    with open(filename, "r") as f:
        state = [int(x) for x in f.readline().rstrip().split(",")]

    return state

def part_1(filename: str, days: int) -> None:
    state = read_input(filename)

    for i in range (days):
        state = [ x - 1 for x in state]

        indices = [ j for j, x in enumerate(state) if x == -1]
        state += len(indices) * [8]

        for idx in indices:
            state[idx] = 6
        #print(f"After {i+1:3d} day{': ' if i == 0 else 's:'} {state}")
        
    print(len(state))

def part_2(filename: str, days: int) -> None:
    state = np.array(read_input(filename), dtype=np.byte)

    for i in range (days):
        print(i)
        state = np.array([ x - 1 for x in state], dtype=np.byte)

        #indices = np.array([ j for j, x in enumerate(state) if x == -1], dtype=np.byte)
        indices = np.where(state == -1)[0]
        appendix = np.full(len(indices), fill_value=8, dtype=np.byte)

        for idx in indices:
            state[idx] = 6

        state = np.concatenate((state, appendix), axis=0)
        
        #print(f"After {i+1:3d} day{': ' if i == 0 else 's:'} {state}")
        #print(state.size)
        
    print(state.size)


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename, 80)
    part_2(filename, 256)