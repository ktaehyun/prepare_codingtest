from collections import deque

def solution(maps):
    
    q = deque()
    q.append((0,0))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0]) or maps[nx][ny]==0:
                continue
            elif maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append((nx,ny))
                
    ans = maps[len(maps)-1][len(maps[0])-1]
    return -1 if ans==1 else ans