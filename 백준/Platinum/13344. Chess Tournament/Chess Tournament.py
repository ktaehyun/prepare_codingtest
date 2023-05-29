import sys
from collections import deque


def find(x):
    global parents

    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(x, y):
    global rank, parents

    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] > rank[y]:
            x, y = y, x

        parents[x] = y

        if rank[x] == rank[y]:
            rank[y] += 1


n, m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n)]
in_degree = [0] * n

parents = [0] * n
rank = [1] * n
for i in range(n):
    parents[i] = i

tmp = []
for _ in range(m):
    a, op, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)

    if op == '>':
        tmp.append([a, b])
    else:
        union(a, b)

for a, b in tmp:
    a = find(a)
    b = find(b)

    adj_list[a].append(b)
    in_degree[b] += 1

cnt = 0
q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    cnt += 1

    for there in adj_list[cur]:
        in_degree[there] -= 1
        if in_degree[there] == 0:
            q.append(there)

print("consistent" if cnt == n else "inconsistent")