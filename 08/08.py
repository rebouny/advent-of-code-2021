#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class Riddle(object):
    def __init__(self, codes, values):
        self.codes = [''.join(sorted(c)) for c in codes]
        self.values = [''.join(sorted(v)) for v in values]

    def solve(self):
        self.decodes = dict()

        self.decodes[1] = list(filter(lambda x: len(x) == 2, self.codes))[0]
        self.decodes[4] = list(filter(lambda x: len(x) == 4, self.codes))[0]
        self.decodes[7] = list(filter(lambda x: len(x) == 3, self.codes))[0]
        self.decodes[8] = list(filter(lambda x: len(x) == 7, self.codes))[0]

        self.decodes[9] = self._decode_9()
        self.decodes[3] = self._decode_3()
        self.decodes[0] = self._decode_0()
        self.decodes[6] = self._decode_6()
        self.decodes[5] = self._decode_5()
        self.decodes[2] = self._decode_2()

    def get_digits(self):
        return [ list(self.decodes.keys())[list(self.decodes.values()).index(value)] for value in self.values ]

    def _decode_9(self):
        length_6  = list(filter(lambda x: len(x) == 6, self.codes))
        return [x for x in length_6 if set(self.decodes[4]).issubset(set(x))][0]

    def _decode_3(self):
        length_5 = list(filter(lambda x: len(x) == 5, self.codes))
        return [x for x in length_5 if set(self.decodes[1]).issubset(set(x))][0]

    def _decode_0(self):
        length_6 = list(filter(lambda x: len(x) == 6, self.codes))
        length_6.remove(self.decodes[9])
        return [x for x in length_6 if set(self.decodes[7]).issubset(set(x))][0]

    def _decode_6(self):
        length_6 = list(filter(lambda x: len(x) == 6, self.codes))
        length_6.remove(self.decodes[9])
        length_6.remove(self.decodes[0])
        return length_6[0]

    def _decode_5(self):
        length_5  = list(filter(lambda x: len(x) == 5, self.codes))
        length_5.remove(self.decodes[3])
        return [x for x in length_5 if len(set(self.decodes[6]).symmetric_difference(set(x))) == 1][0]

    def _decode_2(self):
        length_5  = list(filter(lambda x: len(x) == 5, self.codes))
        length_5.remove(self.decodes[3])
        length_5.remove(self.decodes[5])
        return length_5[0]


def read_input(filename: str):
    riddles = list()

    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            codes, values = line.rstrip().split(" | ", 2)
            riddles.append(Riddle(codes.split(" "), values.split(" ")))

    return riddles


def part_1(filename: str) -> None:
    riddles = read_input(filename)

    sum_easy_codes = 0

    for riddle in riddles:
        riddle.solve()

        digits = riddle.get_digits()

        sum_easy_codes += digits.count(1) + digits.count(4) + digits.count(7) + digits.count(8)

    print(sum_easy_codes)

def part_2(filename: str) -> None:
    riddles = read_input(filename)

    sum_codes = 0

    for riddle in riddles:
        riddle.solve()

        digits = riddle.get_digits()

        sum_codes += int(''.join(map(str, digits)))

    print(sum_codes)

if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)