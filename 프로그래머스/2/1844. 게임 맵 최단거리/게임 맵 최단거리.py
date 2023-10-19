from collections import deque

def solution(maps):
    
    result = []
    
    n, m = len(maps[0]), len(maps)
    visited = [[False for col in range(n)] for row in range(m)]
    visited[0][0] = True
    
    queue = deque([(0,0,1)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x, y, distance = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==False and maps[nx][ny]==1:
                queue.append((nx, ny, distance+1))
                visited[nx][ny] = True
            if nx==m-1 and ny==n-1:
                result.append(distance+1)
    
    if result:
        return min(result)
    return -1