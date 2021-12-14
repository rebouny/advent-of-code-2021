#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Graph(object):
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def all_vertices(self):
        return set(self.gdict.keys())

    def add_edge(self, edge):
        edge = set(edge)
        (vertex_a, vertex_b) = tuple(edge)
        for x, y in [(vertex_a, vertex_b), (vertex_b, vertex_a)]:
            if x in self.gdict:
                self.gdict[x].append(y)
            else:
                self.gdict[x] = [y]
    
    def find_all_paths(self, start_vertex, end_vertex, path=[], twice=None):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.gdict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if (vertex not in path) or vertex.isupper() or (vertex == twice and path.count(vertex) < 2):
                # either not visited or multi-visit uppercase node
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path,
                                                     twice)
                for p in extended_paths: 
                    paths.append(p)    

        return paths

def can_added_twice(path, vertex: str) -> bool:
    if vertex in [ 'start', 'end']:
        return False
    if vertex.isupper():
        return True
    return path.count(vertex) < 2


def read_graph(filename: str):
    g = Graph()

    with open(filename, "r") as f:
        lines = f.read().splitlines()

    for line in lines:
        (start, end) = line.split("-", 2)
        g.add_edge({start, end})

    return g


def part_1(filename: str) -> None:
    graph = read_graph(filename)

    path = graph.find_all_paths("start", "end")
    
    print(len(path))

def part_2(filename: str) -> None:
    graph = read_graph(filename)

    small_caves = set(filter(lambda x: x.islower() and x not in ['start', 'end'], graph.all_vertices()))
    combined_paths = set()
    for sc in small_caves:
        path = graph.find_all_paths("start", "end", [], sc)
        for p in path:
            combined_paths.add(",".join(p))
        
    print(len(combined_paths))


if __name__ == "__main__":
    filename = sys.argv[1]

    part_1(filename)
    part_2(filename)