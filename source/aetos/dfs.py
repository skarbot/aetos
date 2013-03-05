# Corsea Algorithms problem 4
'''
Given a graph input with nodes as first row and connected edges 
as second row perform a depth first search algorithm to compute
the stongly connected component.

'''

import sys
from collections import deque

sys.setrecursionlimit(547483647)

#: Expolored nodes
EXPLORED = set()

#: Time
TIME = 1

#: Stack
STACK = []

def dfs(nodes, current_node, stack=None):
    '''For a given directed graph with *nodes* run the kosarajus two step
    approch to calculate strongly connected components.
    *explored* list of explored nodes.
    *direction* forward/reverse direction to perform dfs.

    '''
    global EXPLORED
    global STACK

    counter = 1
    que = deque([current_node])

    if not stack:
        stack = deque()

    while que:
        counter = 1
        vertex = que[-1]
        if vertex in EXPLORED:
            que.pop()
            if not vertex in stack:
                stack.append(vertex)
        else:
            EXPLORED.append(vertex)
            neighbor_vertex = nodes.get(vertex, [])

            for each_vertex in neighbor_vertex:
                if not each_vertex in EXPLORED:
                    que.append(each_vertex)
                    counter = 0
            if counter:
                stack.append(vertex)
                que.pop()
        print 'Length of Que: {0}'.format(len(que))
    return stack

def kosaraju_algorithm(file):
    '''For file containing the edges of a directed graph. Every row indicates
    an edge, the vertex label in first column is the tail and the vertex label
    in second column is the head (recall the graph is directed, and the edges
    are directed from the first column vertex to the second column vertex). So
    for example, the 11th row looks liks : "2 47646". This just means that the
    vertex with label 2 has an outgoing edge to the vertex with label 47646.

    '''
    global EXPLORED
    global STACK

    STACK = deque()
    EXPLORED = deque()
    forward = {}
    reverse = {}
    leader = 0

    with open(file) as graph:
        for line in graph:
            variables = line.split(' ')
            variables = [int(variables[0]), int(variables[1])]

            forward[variables[0]] = forward.get(variables[0], [])
            forward[variables[0]].append(variables[1])

            # Reverse data
            reverse[variables[1]] = reverse.get(variables[1], [])
            reverse[variables[1]].append(variables[0])

            if variables[0] >  leader:
                leader = variables[0]
            if variables[1] >= leader:
                leader = variables[1]

    print 'Graph computed-----------'
    # Perform kosaraju algorithm 
    # Dfs on reverse search
    print leader
    print len(reverse.keys())
    print len(forward.keys())
    for i in range(leader, 0, -1):
        if not i in EXPLORED:
            print i
            value = dfs(reverse, i, [])
            STACK.extend(value)

    data = {}
    EXPLORED.clear()
    print 'Leader: {0}'.format(leader)
    print 'Stack length : {0}'.format(len(STACK))

    for i in range(len(STACK)-1, -1, -1):
        if not STACK[i] in EXPLORED:
            print STACK[i]
            data[STACK[i]] = dfs(forward, STACK[i])

    print 'We are done'
    size = []

    for value in data.values():
        # Compute size
        size.append(len(value))
    size.sort(reverse=True)
    print data
    return size[:5]

