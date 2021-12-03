#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys 
from typing import NamedTuple

def part_1(filename: str):
    with open(filename, "r") as f:
        c = [tuple(l.rstrip().split(' ')) for l in f ]

    sum_forward = sum(int(x[1]) for x in filter(lambda x: 'forward' == x[0], c))
    sum_up = sum(int(x[1]) for x in filter(lambda x: 'up' == x[0], c))
    sum_down = sum(int(x[1]) for x in filter(lambda x: 'down' == x[0], c))

    print(sum_forward * (sum_down - sum_up))

class State(NamedTuple):
    """submarien's state"""
    horizontal: int
    aim: int
    depth: int

def part_2(filename: str):

    def forward(state: State, value) -> State: #NOSONAR
        return State(state.horizontal + value, state.aim, state.depth + value * state.aim)
    def up(state: State, value) -> State: #NOSONAR
        return State(state.horizontal, state.aim - value, state.depth)
    def down(state: State, value) -> State: #NOSONAR
        return State(state.horizontal, state.aim + value, state.depth)

    with open(filename, "r") as f:
        c = [tuple(l.rstrip().split(' ')) for l in f ]

    state = State(0, 0, 0)
    for i in c:
        state = locals()[i[0]](state, int(i[1]))

    print (state.horizontal * state.depth)


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)
