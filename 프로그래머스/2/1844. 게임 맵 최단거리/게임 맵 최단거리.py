from collections import deque

def solution(maps):
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=n or ny<0 or ny>=m or maps[nx][ny]==0:
                continue
            elif maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    ans = maps[n-1][m-1]
    
    return -1 if ans==1 else ans