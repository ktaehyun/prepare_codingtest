n, k = map(int, input().split())

bags = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    bags.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bags[i][0]
        v = bags[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])