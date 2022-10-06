# # d = [동, 서, 남, 북]
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# result = []
    
# def solution(maps):
#     n,m = len(maps),len(maps[0])
#     q = [[0 for _ in range(m)] for _ in range(n)]
#     q[0][0] = 1
#     progress(maps,n,m,q,0,0,1)
#     if result:
#         return min(result)
#     else:
#         return -1
    
# def progress(maps,n,m,q,x,y,count):
#     global result
#     for d in range(4) :
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if nx<0 or nx>=n or ny<0 or ny>=m or q[nx][ny]==1 or maps[nx][ny]==0 :
#             continue
#         count += 1
#         q[nx][ny] = 1
#         if nx==n-1 and ny==m-1 :
#             result.append(count)
#             break
#         progress(maps,n,m,q,nx,ny,count)




from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[False for col in range(n)] for row in range(m)]
    visited[0][0] = True

    queue = deque()
    queue.append((0,0,1))

    while queue:
        yIndex, xIndex, distance = queue.popleft()
        if xIndex == n-1 and yIndex == m-1:
            return distance

        if 0<=xIndex+1<n and visited[yIndex][xIndex+1] == False and maps[yIndex][xIndex+1] == 1:
            queue.append((yIndex, xIndex+1, distance+1))
            visited[yIndex][xIndex+1] = True
        if 0<=yIndex+1<m and visited[yIndex+1][xIndex] == False and maps[yIndex+1][xIndex] == 1:
            queue.append((yIndex+1, xIndex, distance+1))
            visited[yIndex+1][xIndex] = True
        if 0<=xIndex-1<n and visited[yIndex][xIndex-1] == False and maps[yIndex][xIndex-1] == 1:
            queue.append((yIndex, xIndex-1, distance+1))
            visited[yIndex][xIndex-1] = True
        if 0<=yIndex-1<m and visited[yIndex-1][xIndex] == False and maps[yIndex-1][xIndex] == 1:
            queue.append((yIndex-1, xIndex, distance+1))
            visited[yIndex-1][xIndex] = True

    return -1