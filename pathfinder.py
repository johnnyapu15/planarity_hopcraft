
# Input: array of adj_list
adj_list = [[0], [1], [2], [0, 2], [0, 2]]

# Define main cycle c
c = []
c.append(0)
for idx, li in enumerate(adj_list):
    for v in enumerate(li):
        if idx < v[0]:
            c.append(v)
        