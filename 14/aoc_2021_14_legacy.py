#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import List, Tuple, Dict
import copy

def read_data(filename: str) -> Tuple[str,Dict[str,str]]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    template = []
    rules = {}

    idx = lines.index("")

    for line in lines[0:idx]:
        template = line   
    for line in lines[idx+1:]:
        ab, c = line.split(" -> ", 2)
        rules[ab] = c

    return template, rules


def calc(template: str)-> int:
    chars = set([x for x in template ])

    max_c = max (map(lambda x: (template.count(x), x), chars))
    min_c = min (map(lambda x: (template.count(x), x), chars))
    
    return max_c[0] - min_c[0]



def process(template: str, rules: Dict[str, str], counts: Dict[str,Tuple[str,int]]=None) -> str:
    result = list()

    for i in range(1, len(template)):
        s = template[i-1:i+1]
        if s in rules:
            result.append("".join([template[i-1], rules[s]]))
            if counts:
                v, c = counts[s]
                counts[s] = (v, c + 1)
        if i == len(template) -1:
            result.append(template[i])

    return "".join(result)


def part_1(filename: str, n: int) -> None:
    template, rules = read_data(filename)

    s = template
    for _ in range(n):
        s = process(s, rules)

    print(calc(s))


def part_2(filename: str, n: str) -> None:
    template, rules = read_data(filename)

    s = template
    for i in range(n):
        #print(f"step {i+1 } out of {n}")
        s = process(s, rules)
        h_c = s.count('H')
        b_c = s.count('B')
        n_c = s.count('N')
        c_c = s.count('C')

        print(f"{(i+1):3}: H({h_c:6}) B({b_c:6}) N({n_c:6}) C({c_c:6}): - {(h_c - c_c):6} len({len(s):6})")

    print(calc(s))


def part_n(filename: str, n: int) -> None:
    template, rules = read_data(filename)

    counts = dict()
    list_counts = list()
    for k,v in rules.items():
        counts[k] = (v, 0)

    # init count dict
    c = dict()
    for k in rules.keys():
        c[k] = 0
    c['NN'] = 1
    c['NC'] = 1
    c['CB'] = 1

    # init modification dict
    m = dict()
    for k, v in rules.items():
        m[k] = (k[0] + v, v + k[1])

    s = template
    print(s)
    print(" ".join([f"{k:>6}" for k,v in counts.items()]))
    print(" ".join([f"{v[0]:>3}{v[1]:>3}" for k,v in m.items()]))
    print("-" * len(counts) * 7)

    for i in range(n):
        #print(f"step {i+1 } out of {n}")
        #s = process(s, rules, counts)
        list_counts.append(copy.deepcopy(counts))
        _c = copy.deepcopy(c)
        for k, v in _c.items():
            left, right = m[k]
            c[left] += v
            c[right] += v 

        print(f"{i+1:3}: ")
        print(" ".join([f"{v:>6}" for k,v in c.items()]))
        s = { 'N': 0, 'H' : 0, 'C': 0, 'B': 0}
        for k, v in c.items():
            s[k[0]] += v
            s[k[1]] += v
        print(s)

#    print(" ".join([f"{k:>6}" for k,v in counts.items()]))
 #   print(" ".join([f"{v[0]:>6}" for k,v in counts.items()]))
  #  print("-" * len(counts) * 7)
   # for i in list_counts:
    #    print(" ".join([f"{v[1]:>6}" for k,v in i.items()]))
    #print("-" * len(counts) * 7)
    #print(" ".join([f"{v:>6}" for k,v in c.items()]))

    s = { 'N': 0, 'H' : 0, 'C': 0, 'B': 0}
    for k, v in c.items():
        s[k[0]] += v
        s[k[1]] += v


    print(s)

    print(max(c.values()))

#    print(calc(s))


if __name__ == "__main__":
    filename = sys.argv[1]

    #part_1(filename, 10)
    #part_2(filename, 40)
    
    part_n(filename, 4)