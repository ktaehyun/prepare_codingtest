n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

# d = [동, 서, 남, 북]
da = [0, 0, 1, -1]
db = [1, -1, 0, 0]

q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append([graph[i][j], i, j])
q.sort(key=lambda x: x[0])

for _ in range(s):
    now_length = len(q)
    count = 0
    while count < now_length:
        count += 1
        vir = q.pop(0)
        vir_num, a, b = vir[0], vir[1], vir[2]
        for d in range(4):
            na = a + da[d]
            nb = b + db[d]
            if 0<=na<n and 0<=nb<n and graph[na][nb]==0:
                graph[na][nb] = vir_num
                q.append([vir_num, na, nb])

print(graph[x-1][y-1])