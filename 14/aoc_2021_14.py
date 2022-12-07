#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-12-05
Purpose: Solves day 06 from advent of code 2022.
"""

from typing import Final


TEST_DATA_PART_01: Final = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


# --------------------------------------------------
def load_data(filename: str):
    """Loads complete input into a string"""
    with open(filename, 'rt', encoding='utf-8') as file:
        return parse_data(file.readlines())


def parse_data(lines):
    """Parses rule-set from input file"""
    template = lines[0].rstrip()
    rules = { line[0:2]: line[6] for line in lines[2:]}

    return template, rules


def solve(template, rules, steps):
    """Counts character occurrance on polymer transposition"""
    track = { k: 0 for k in rules }

    for key in [template[i-1:i + 1] for i in range(1, len(template))]:
        track[key] += 1

    added = {c: template.count(c) for c in set(template)}

    for _ in range(0, steps):
        cpy = {}

        for key in filter(lambda x: track.get(x, 0) > 0, track):
            rpl = rules[key]
            left = key[0] + rpl
            right = rpl + key[1]

            cpy[left] = cpy.get(left, 0) + track[key]
            cpy[right] = cpy.get(right, 0) + track[key]

            added[rpl] = added.get(rpl, 0) + track[key]

        track = cpy.copy()

    return max(added.values()) - min(added.values())


# --------------------------------------------------
def test_solve():
    """Tests solving strategy"""
    template, rules = parse_data(TEST_DATA_PART_01.split('\n'))

    assert 1588 == solve(template, rules, 10)


# --------------------------------------------------
def main() -> None:
    """Main wrapper."""
    template, rules = load_data('./input')

    print(solve(template, rules, 10))
    print(solve(template, rules, 40))


if __name__ == '__main__':
    main()


# --------------------------------------------------
# obsolete code with not working strategies
# --------------------------------------------------

MAP_C_N: Final = {'B': 0, 'F': 1, 'H': 2, 'O': 3, 'S': 4, 'P': 5, 'C': 6, 'K': 7, 'V': 8, 'N': 9}
MAP_N_C: Final = { 0: 'B', 1: 'F', 2: 'H', 3: 'O', 4: 'S', 5: 'P', 6: 'C', 7: 'K', 8: 'V', 9: 'N'}
MAP_N_N: Final = {62: 0, 22: 9, 60: 2, 92: 6, 20: 6, 26: 0, 29: 6, 99: 6, 2: 2, 96: 0, 90: 0, 9: 0,
                  0: 9, 6: 0, 66: 9, 69: 6}


def parse_data__with_conversion(lines):
    """Parses rules and directly translates ruleset to numbers"""
    template = lines[0].rstrip()
    rules = { line[0:2]: line[6] for line in lines[2:]}

    n_rules = { 10 * MAP_C_N[k[0]] + MAP_C_N[k[1]]: MAP_C_N[v] for k, v in rules.items()}

    return template, rules, n_rules


def part_01(template, rules, steps) -> int:
    """Solves both parts"""
    polymer = template
    for _ in range(steps):
        polymer = step(polymer, rules)

    counts = sorted([polymer.count(c) for c in set(polymer)])

    return counts[-1] - counts[0]


def step(polymer, rules):
    """Calculates a step for polymer 'traditional' style"""
    poly = [polymer[i-1:i+1] for i in range(1, len(polymer))]

    return polymer[0] + "".join(map(lambda x: f'{rules[x]}{x[1]}', poly))


def step_n(n_polymer: int, rules):
    """Calculates n-th step for polymer"""
    num = n_polymer
    ret_num = 0
    power = 1
    while num > 0:
        if num < 10:
            ret_num += num * power
            num = 0
        else:
            last = num % 10
            num = num // 10
            ins = rules[10 * (num%10) + last]

            ret_num += power * last
            power *= 10
            ret_num += power * ins
            power *= 10

    return ret_num


def c_to_n(polymer):
    """Maps chars to numbers"""
    return "".join(map(lambda x: str(MAP_C_N[x]), polymer))


def count_n(n_polymer):
    """Counts occurrance of a number in numeric polymer"""
    num = n_polymer

    cnt_num = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }

    while num > 0:
        last = num % 10
        cnt_num[last] += 1
        num = num // 10

    return sorted(filter(lambda x: x > 0, [value for _, value in cnt_num.items()]))


def part_02(template, rules, steps):
    """Solution for part to using number mapping instead of chars.
    This solves to problem of vast memory consumption but not the
    one of endlessly runtime. So honestly it doesn't 'solve' anything
    at all.
    """
    polymer = template
    n_polymer = int(c_to_n(polymer))

    for i in range(steps):
        n_polymer = step_n(n_polymer, rules)

        print(f'{i}')

    counts = count_n(n_polymer)

    return counts[-1] - counts[0]


def test_steps():
    """Tests part 01"""
    template, rules = parse_data(TEST_DATA_PART_01.split('\n'))

    step1 = step(template, rules)
    assert "NCNBCHB" == step1

    step2 = step(step1, rules)
    assert "NBCCNBBBCBHCB" == step2

    step3 = step(step2, rules)
    assert "NBBBCNCCNBBNBNBBCHBHHBCHB" == step3

    step4 = step(step3, rules)
    assert "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB" == step4
