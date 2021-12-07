#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from statistics import median as md


def get_data(filename: str):
    with open(filename, "r") as f:
        return list(map(int, f.readline().rstrip().split(",")))


def part_1(filename: str) -> None:
    data = get_data(filename)

    median = int(md(data))
    fuel = sum(abs(x - median) for x in data)
    print (fuel)


def part_2(filename: str) -> None:
    data = get_data(filename)
    
    # brute force
    data_max = max(data)

    fuel = sum(sum(range(1, abs(x - 0) + 1)) for x in data)
    for i in range(1, data_max + 1):
        fuel = min(fuel, sum(sum(range(1, abs(x - i) + 1)) for x in data))

    print(fuel)


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)

