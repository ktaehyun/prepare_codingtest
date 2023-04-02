from collections import deque


n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
    
d_s = []
for _ in range(m):
    d_s.append(list(map(int, input().split())))


# d = [left, left_up, up, rigth_up, right, right_down, down, left_down]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

A = deque([(n-1,0), (n-1,1), (n-2,0), (n-2,1)])

def limitExpand(nn):
    if nn < 0:
        nn += n
    elif nn >= n:
        nn -= n
    else:
        return nn
    return limitExpand(nn)

def Cycle(a, d, s, check):
    next_xy = deque([])
    while a:
        x, y = a.popleft()
        nx = x + (dx[d] * s)
        nx = limitExpand(nx)
        ny = y + (dy[d] * s)
        ny = limitExpand(ny)
        maps[nx][ny] += 1
        next_xy.append((nx, ny))
        check.append((nx,ny))
        
    secondCycle(next_xy)
        
    return check

def secondCycle(x_y):
    while x_y:
        nx, ny = x_y.popleft()
        count = 0
        if nx-1>=0 and ny-1>=0 and maps[nx-1][ny-1]!=0:
            count += 1
        if nx-1>=0 and ny+1<n and maps[nx-1][ny+1]!=0:
            count += 1
        if nx+1<n and ny+1<n and maps[nx+1][ny+1]!=0:
            count += 1
        if nx+1<n and ny-1>=0 and maps[nx+1][ny-1]!=0:
            count += 1
        maps[nx][ny] += count

def Process(a, d, s):
    check = Cycle(a, d, s, [])
    temp = deque([])
    for i, lst in enumerate(maps):
        for j, water in enumerate(lst):
            if water>=2 and (i,j) not in check:
                maps[i][j] = water - 2
                temp.append((i,j))
                
    return temp

for ds in d_s:
    A = Process(A, ds[0]-1, ds[1])


result = 0
for sum_maps in maps:
    result += sum(sum_maps)

print(result)