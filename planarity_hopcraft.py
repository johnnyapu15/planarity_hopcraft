
# # Input: array of adj_list
# adj_list = [[1], [2], [3], [0, 2], [0, 2]]
# s = 0

# global s
# # Define main cycle c
# c = []
# c.append(0)
# s += 1
# for idx, li in enumerate(adj_list):
#     for i, v in enumerate(li):
#         if idx < v:
#             c.append(v)
#             s += 1



# paths = []


def DFS_hopcraft(v, u):
    global isArc
    global LOWPT
    global NUMBER
    global n
    global adj_list_default
    NUMBER[v] = n + 1
    n += 1
    # Statement a
    LOWPT[v] = [v,v]
    for idx, w in enumerate(adj_list_default[v]):
        if NUMBER[w] == -1:
            # a is a new vertex.
            isArc[str([v, w])] = True # if true then [v, w] is arc.
            DFS_hopcraft(w, v)
            # Statement b
            if LOWPT[w][0] < LOWPT[v][0]:
                LOWPT[v][1] = min(LOWPT[v][0], LOWPT[w][1])
                LOWPT[v][0] = LOWPT[w][0]
            elif LOWPT[w][0] == LOWPT[v][0]:
                LOWPT[v][1] = min(LOWPT[v][1], LOWPT[w][1])
            else:
                LOWPT[v][1] = min(LOWPT[v][1], LOWPT[w][0])
        
        elif NUMBER[w] < NUMBER[v] & w != u:
            isArc[str([v, w])] = False 
            # Statement c
            if NUMBER[w] < LOWPT[v][0]:
                LOWPT[v][1] = LOWPT[v][0]
                LOWPT[v][0] = NUMBER[w]
            elif NUMBER[w] > LOWPT[v][0]:
                LOWPT[v][1] = min(LOWPT[v][1], NUMBER[w])

def PHI(edge):
    global LOWPT
    if edge[0] > edge[1]:
        return 2*edge[1]
    elif edge[0] < edge[1] & LOWPT[edge[1]][1] >= edge[0]:
        return 2*LOWPT[edge[1]][0]
    else:
        return 2*LOWPT[edge[1]][0] + 1

def contruct_ordered_adj_list():
    global V
    global EDGES
    BUCKET = []
    [BUCKET.append([]) for i in range(2*V + 1)]
    
    for idx, e in enumerate(EDGES):
        tmp = PHI(e)
        BUCKET[tmp].append(e)
    ret = []
    [ret.append([]) for i in range(V)]
    for idx, es in enumerate(BUCKET):
        for i, e in enumerate(es):
            ret[e[0]].append(e[1])
    return ret

def findSv(v):
    # S_v is the set of vertices reached by fronds from descendants of v.
    global adj_list_default
    ret = []
    for idx, u in enumerate(adj_list_default[v]):
        if v < u:
            for idx2, w in enumerate(adj_list_default[u]):
                if w < u:
                    ret.append(w)
    return ret

def LOWPT1(v):
    sv = findSv(v)
    sv.append(v)
    return min(sv)

def LOWPT2(v):
    sv = findSv(v)
    lowpt1 = LOWPT1(v)
    sv.remove(lowpt1)
    sv.append(v)
    return min(sv)


EDGES = [[]]
adj_list_default = [[]]
V = 16
isArc = dict()
LOWPT = []
[LOWPT.append([0, 0]) for i in range(V)]
NUMBER = [-1]*(V)
n = -1
s = 0


EDGES = [[0, 1], [0, 11], [1, 0], [1, 2], [1, 15], [2, 1], [2, 3], [2, 15], [3, 2], [3, 4], [3, 6], [4, 3], [4, 5], [4, 14], [5,4], [5, 6], [5, 7], [6, 3], [6, 5], [6, 7], [7, 5], [7, 6], [7, 8], [8, 7], [8, 9], [8, 14], [9, 8], [9, 10], [9, 15], [10, 9], [10, 11], [10, 13], [11, 0], [11, 10], [11, 12], [12, 11], [12, 13], [12, 14], [13, 10], [13, 12], [13, 14], [14,4], [14, 8], [14, 12], [14, 13], [15, 1], [15, 2], [15, 9]]
#EDGES = [[0, 1], [0, 11], [1, 2], [1, 15], [2, 3], [2, 15], [3, 4],[3, 6], [4, 5], [4, 14], [5, 6], [5, 7], [6, 7], [7, 8], [8, 9], [8, 14], [9, 10], [9, 15], [10, 11], [10, 13], [11, 12], [12, 13], [12, 14], [13, 14]]
adj_list_default = [[1, 11], [0, 2, 15], [1, 3, 15], [2, 4, 6], [3, 5, 14], [4, 6, 7], [3, 5, 7], [5, 6, 8], [7, 9, 14], [8, 10, 15], [9, 11, 13], [0, 10, 12], [11, 13, 14], [10, 12, 14], [4, 8, 12, 13], [1, 2, 9]]
#adj_list_default = [],[2, 64], [1, 3, 47], [2, 4, 32], [3, 5], [4, 6, 52], [5, 7, 64], [6, 8], [7, 9, 54], [8, 10, 60], [9, 11, 63], [10, 12], [11, 13, 58], [12, 14], [13, 15, 42], [14, 16, 49], [15, 17, 59], [16, 18, 61], [17, 19, 62], [18, 20, 48], [19, 21, 24], [20, 22, 38], [21, 23, 50], [22, 24, 25], [20, 23, 25], [23, 24, 26], [25, 27, 51], [26, 28, 62], [27, 29, 53], [28, 30, 51], [29, 31, 52], [30, 32, 51], [3, 31, 33], [32, 34], [33, 35, 46], [34, 36, 50], [35, 37], [36, 38, 44], [21, 37, 39], [38, 40], [39, 41, 48], [40, 42, 43], [14, 41], [41, 44], [37, 43, 45], [44, 46], [34, 45, 47], [2, 46], [19, 40, 49], [15, 48], [22, 35, 51], [26, 29, 31, 50], [5, 30, 53], [28, 52, 54], [8, 53, 55], [54, 56], [55, 57, 61], [56, 58, 60], [12, 57, 59], [16, 58], [9, 57], [17, 56, 62], [18, 27, 61], [10, 64], [1, 6, 63]
s = 0
DFS_hopcraft(s, -1)
adj_list = contruct_ordered_adj_list()



paths = []

def pathfinder_hopcraft(pre, v):
    global s
    global cur_path
    global paths
    global adj_list
    for idx, w in enumerate(adj_list[v]):
        if w != pre:
            if v < w:
                if s == -1:
                    s = v
                    #paths.append(cur_path)
                    cur_path = []
                cur_path.append(w)
                pathfinder_hopcraft(v, w)
            else:
                # v - -> w
                if s == -1:
                    s = v
                    #paths.append(cur_path)
                    cur_path = [] 
                cur_path.append(w)
                paths.append(cur_path)
                s = -1

# paths = []
cur_path = []
s = -1
pathfinder_hopcraft(-1, 0)
