# Corsea Algorithms problem 4
'''
Given a graph input with nodes as first row and connected edges 
as second row perform a depth first search algorithm to compute
the stongly connected component.

'''

#: Expolored nodes
EXPLORED = []

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

    if not stack:
        stack = []

    EXPLORED.append(current_node)

    for edge in nodes[current_node]:
        if not edge in EXPLORED:
            stack = dfs(nodes, edge, stack)

    stack.append(current_node)
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
    EXPLORED = []
    forward = {}
    reverse = {}
    leader = 0
    with open(file) as graph:
        for line in graph:
            variables = line.split(' ')

            if int(variables[0]) in forward.keys():
                forward[int(variables[0])].append(int(variables[1]))
            else:
                forward[int(variables[0])] = [int(variables[1])]

            # Reverse data
            if not int(variables[1]) in reverse.keys():
                reverse[int(variables[1])] = [int(variables[0])]
            else:
                reverse[int(variables[1])].append(int(variables[0]))
            leader = int(variables[0])

    # Perform kosaraju algorithm 
    # Dfs on reverse search
    for i in range(leader, 0, -1):
        if not i in EXPLORED:
            value = dfs(reverse, i, [])
            STACK.extend(value)

    data = {}
    EXPLORED = []

    for i in range(len(STACK)-1, 0, -1):
        if not STACK[i] in EXPLORED:
            data[STACK[i]] = dfs(forward, STACK[i])

    size = [0,0,0,0]
    for value in data.values():
        # Compute size
        size.append(len(value))
    size.sort(reverse=True)
    return size[:5]

