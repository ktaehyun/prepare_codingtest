def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    result = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])

    for node1, node2, cost in costs:
        if find_parent(parent, node1) != find_parent(parent, node2):
            union_parent(parent, node1, node2)
            result += cost 

    return result