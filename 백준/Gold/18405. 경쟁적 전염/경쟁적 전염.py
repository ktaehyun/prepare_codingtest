n, k = map(int, input().split())
maps, virusxy = [], []
for a in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for b, v in enumerate(tmp):
        if v != 0:
            virusxy.append((v, a, b))
s, x, y = map(int, input().split())    # s초 후, x,y 좌표의 숫자

# d = [동,서,남,북]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

virusxy.sort(key = lambda x: x[0])
for _ in range(s):
    cycle = len(virusxy)
    count = 0
    while count < cycle:
        count += 1
        virus, a, b = virusxy.pop(0)
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n and maps[nx][ny]==0:
                maps[nx][ny] = virus
                virusxy.append((virus, nx, ny))
        
print(maps[x-1][y-1])