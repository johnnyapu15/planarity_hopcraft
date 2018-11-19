import numpy as np
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
# Initiation some valuesb 
adj_list = []
[adj_list.append(list()) for i in range(num)]
arc_stack = []
j = 0 # Next vertex index of m
i = 0 # Current vertex index of m
idx_new = [-1]*num
idx = 0
# 1. Find arc
def findArc(i):
    while (1 in m[i]):
        j = m[i].index(1)
        idx = idx_new.__len__() - idx_new.count(-1)
        arc_stack.append(idx)
        print(arc_stack)
        if idx_new[j] == -1:
            adj_list[idx].append(idx+1)
            m[i][j] = 0
            m[j][i] = 0
            idx_new[i] = idx
            i = j 
        else:
            idx_new[i] = idx
            break

print(m)
print(adj_list)
print(idx_new)
# 2. Find fronds. ( = backtracking)
# Current i is last vertex of ARC.
def findFronds():
    while(arc_stack.__len__() > 0):
        # idx_new[i]: new index of vertex in m by DFS
        # if idx_new[i] is -1 then ? to idx_new[i] is arc.
        ## ? is maybe m[i].index(1).
        i = arc_stack[-1]
        while(1 in m[i]):
            j = m[i].index(1)
            # when other arc
            if (j > i):
                findArc(i)
                # idx_new[j] = idx
                # idx += 1
            else:
                adj_list[i].append(j)
            m[i][j] = 0
            m[j][i] = 0
        arc_stack.pop()

# Find first arc
findArc(i) 
findFronds()
