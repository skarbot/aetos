import copy
import random


MIN_CUT=0


def open_file(filepath):
   graph = {}
   with open(filepath) as filedata:
        for each in filedata:
            vertex = []
            vertex = [int(vertex) for vertex in each.split()]
            graph[vertex[0]] = vertex[1:]
   return graph

def main():
    global MIN_CUT
    filepath = '/home/Kartikeyan.Sundaraja/workspace/aetos/test/data/kargerMinCut.txt'
    graph = open_file(filepath)
    min_cut = 0
    for i in range(0, 201):
        min_cut_temp = karger(copy.deepcopy(graph))
        print min_cut_temp
        if min_cut_temp < min_cut:
            min_cut = min_cut_temp
    return min_cut


def choose_random_edge(g): #return an edge represented by 2 ints
    v1= g.keys() [random.randint(0,len(g)-1)]
    v2= g[v1] [random.randint(0,len(g[v1])-1)]
    return v1, v2


def karger_step(g):
    v1,v2= choose_random_edge(g)

    #1. attach v2's list to v1
    g[v1].extend(g[v2])

    #2. replace all appearance of v2 as v1
    for x in g[v2]:
        lst=g[x]
        for i in range(0,len(lst)):
            if lst[i]==v2:
                lst[i]=v1

    #3.remove self-loop
    while v1 in g[v1]:
        g[v1].remove(v1)
    #4. remove v2's list
    del g[v2]

def karger(g):
    while len(g) > 2:
        karger_step(g)
    return len(g[g.keys()[0]])

