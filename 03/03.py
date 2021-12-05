#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def read_data(filename: str):
    with open(filename, "r") as f:
        # read "bit"-field length from first line
        line = f.readline().rstrip()
        s = list([int(x) for x in line])
        count = 1

        for line in f:
            l = list(int(x) for x in line.rstrip())
            s = [a + b for a, b in zip(l, s)]
            count += 1

        return (s, count)

def part_1(filename: str):
    s, count = read_data(filename)

    gamma = int("".join(["1" if (e > count / 2) else "0" for e in s]), 2)
    epsilon = int("".join(["0" if (e > count / 2) else "1" for e in s]), 2)
    print (gamma * epsilon)


def get_oxygen(data):
    for i in range(len(data[0])):
        count_ones = sum([1 if d[i] == 1 else 0 for d in data])
        most = 1 if count_ones >= len(data) - count_ones else 0
        data = [y for y in (d if d[i] == most else None for d in data) if y is not None]

        if len(data) == 1:
            break
    
    return int("".join(str(d) for d in data[0]), 2)

def get_co2_rating(data):
    for i in range(len(data[0])):
        count_ones = sum([1 if d[i] == 1 else 0 for d in data])
        least = 1 if count_ones < len(data) - count_ones else 0
        data = [y for y in (d if d[i] == least else None for d in data) if y is not None]

        if len(data) == 1:
            break

    return int("".join(str(d) for d in data[0]), 2)


def part_2(filename: str):
    data = list()
    with open(filename, "r") as f:
        for line in f:
            l = list(int(x) for x in line.rstrip())
            data.append(l)

    oxygen = get_oxygen(data)
    co2_rating = get_co2_rating(data)

    life_support_rating = oxygen * co2_rating
    print(life_support_rating)


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)