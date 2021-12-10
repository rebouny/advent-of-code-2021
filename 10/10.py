#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import deque
from typing import List


pendant = { '(': ')', '[': ']', '{': '}', '<': '>' }
r_pendant = { ')': '(', ']': '[', '}': '{', '<': '>' }

score = {')': 3, ']': 57, '}': 1197, '>': 25137 }

c_score = {')': 1, ']': 2, '}': 3, '>': 4 }

def is_open_char(c):
    return c in ['[', '(', '{', '<']

def matches(c, a):
    return pendant[c] == a

def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    return lines

def part_1(filename: str) -> None:
    lines = read_input(filename)

    err = { ']': 0, ')': 0, '}': 0, '>': 0 }
    for line in lines:
#        nav = deque()
#        for c in line:
#            if is_open_char(c):
#                nav.append(c)
#            elif matches(nav[-1], c):
#                nav.pop()
#            else:
#                err[c] = err[c] + 1
#                break
        defect_line, c = has_error(line)
        if (defect_line):
            err[c] = err[c] + 1


    print(sum([v * score[k] for k, v in err.items()]))


def has_error(line):
    nav = deque()
    for c in line:
        if is_open_char(c):
            nav.append(c)
        elif matches(nav[-1], c):
            nav.pop()
        else:
            return True, c

    return False, "".join([n for n in nav])

def part_2(filename: str) -> None:
    lines = read_input(filename)

    scores = list()

    for line in lines:
        #nav = deque()
        #for c in line:
        #    if is_open_char(c):
        #        nav.append(c)
        #    elif matches(nav[-1], c):
        #        nav.pop()
        #    else:
        #        nav.clear()
        #        break
        defect_line, open_chars = has_error(line)
        if defect_line:
            continue

        nav = deque([x for x in open_chars])
        auto_complete = list()
        if len(nav) > 0:
            nav.reverse()
            for c in nav:
                auto_complete.append(pendant[c])

            total = 0
            for c in auto_complete:
                total = 5 * total + c_score[c]

            scores.append(total)

    scores.sort()
    print (scores[int(len(scores) / 2)])

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)