#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def part_1(filename: str):
    with open(filename, "r") as f:
        # read "bit"-field length from first line
        line = f.readline().rstrip()
        s = list([int(x) for x in line])
        count = 1

        for line in f:
            l = list(int(x) for x in line.rstrip())
            s = [a + b for a, b in zip(l, s)]
            count += 1

    gamma = int("".join(["1" if (e > count / 2) else "0" for e in s]), 2)
    epsilon = int("".join(["0" if (e > count / 2) else "1" for e in s]), 2)
    print (gamma * epsilon)


def part_2(filename: str):
    pass        


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)