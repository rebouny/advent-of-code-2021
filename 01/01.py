#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys 


def part_1(filename):

    with open(filename, "r") as f:
        l = [int(line) for line in f]

    print(sum([ 1 for i in range(1, len(l)) if l[i] > l[i-1]]))


def part_2(filename):
    with open(filename, "r") as f:
        l = [int(line) for line in f]

    s = [l[i-2] + l[i-1] + l[i] for i in range(2, len(l))]
    print(sum([ 1 for i in range(1, len(s)) if s[i] > s[i-1]]))


if __name__ == "__main__":
    filename = sys.argv[1]

    #part_2(filename)
    part_1(filename)
    part_2(filename)