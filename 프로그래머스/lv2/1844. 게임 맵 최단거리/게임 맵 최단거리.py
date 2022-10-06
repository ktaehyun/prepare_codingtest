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
