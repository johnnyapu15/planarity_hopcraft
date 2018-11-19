#DFS & Numbering

# m = [
#     [0,0,1,1],
#     [0,0,1,1],
#     [1,1,0,1],
#     [1,1,1,0]
#     ]
m = [
    [0,0,1,1,1],
    [0,0,1,1,0],
    [1,1,0,1,1],
    [1,1,1,0,0],
    [1,0,1,0,0]
    ]

num = m.__len__()
# Initiation some values
adj_list = [] # Adjacency list
[adj_list.append(list()) for i in range(num)]
arc_stack = [] # Stack of arcs

i = 0 # Current vertex index in m
j = 0 # Next vertex index in m

idx_new = [-1]*num # New indexs (for numbering)
idx = -1 # idx means 'The index of next arc vertex'.


def DFS(_i):
    # _i: idx in m index, start point of finding arc
    # It breaks(ends) when the arc is branched.
    print ("findArc: " + str(_i))
    global m
    global idx
    global arc_stack
    idx += 1
    idx_new[_i] = idx 
    arc_stack.append(idx)
    print(arc_stack)
    # has next arc vertex?
    for j in range(num):
        if m[_i][j] == 1:
            # is next arc vertex?
            if idx_new[j] == -1:
                print(_i)
                print(j)
                m[_i][j] = 0
                m[j][_i] = 0
                preVtx = arc_stack[-1] # as new index.
                adj_list[preVtx].append(idx)
                DFS(j)
                return
    findFronds()

def findFronds():
    while (arc_stack.__len__() > 0):
        tmpI = arc_stack[-1]
        i = idx_new.index(tmpI)
        while(1 in m[i]):
            j = m[i].index(1)
            # when other arc
            if (j > i):
                DFS(j)
                # idx_new[j] = idx
                # idx += 1
            else:
                print("Add frond: " + str(i) + " -> " + str(j))
                adj_list[i].append(j)
            m[i][j] = 0
            m[j][i] = 0
        if arc_stack.__len__() > 0:
            arc_stack.pop()   



DFS(0)
