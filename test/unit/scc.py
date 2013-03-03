from aetos import dfs

def test1():
    file = '/home/skar/workspace/aetos/test/data/dfs_kr_test1.txt'
    output = dfs.kosaraju_algorithm(file)
    assert output ==  [3,3,2,0,0]

def test2():
    file = '/home/skar/workspace/aetos/test/data/dfs_kr_test2.txt'
    output = dfs.kosaraju_algorithm(file)
    assert output ==  [4,3,3,1,0]


