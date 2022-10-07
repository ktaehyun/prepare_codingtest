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

# from collections import deque

# def solution(maps):
#     n = len(maps[0])
#     m = len(maps)
#     visited = [[False for col in range(n)] for row in range(m)]
#     visited[0][0] = True

#     queue = deque()
#     queue.append((0,0,1))

#     while queue:
#         yIndex, xIndex, distance = queue.popleft()
#         if xIndex == n-1 and yIndex == m-1:
#             return distance

#         if 0<=xIndex+1<n and visited[yIndex][xIndex+1] == False and maps[yIndex][xIndex+1] == 1:
#             queue.append((yIndex, xIndex+1, distance+1))
#             visited[yIndex][xIndex+1] = True
#         if 0<=yIndex+1<m and visited[yIndex+1][xIndex] == False and maps[yIndex+1][xIndex] == 1:
#             queue.append((yIndex+1, xIndex, distance+1))
#             visited[yIndex+1][xIndex] = True
#         if 0<=xIndex-1<n and visited[yIndex][xIndex-1] == False and maps[yIndex][xIndex-1] == 1:
#             queue.append((yIndex, xIndex-1, distance+1))
#             visited[yIndex][xIndex-1] = True
#         if 0<=yIndex-1<m and visited[yIndex-1][xIndex] == False and maps[yIndex-1][xIndex] == 1:
#             queue.append((yIndex-1, xIndex, distance+1))
#             visited[yIndex-1][xIndex] = True

#     return -1