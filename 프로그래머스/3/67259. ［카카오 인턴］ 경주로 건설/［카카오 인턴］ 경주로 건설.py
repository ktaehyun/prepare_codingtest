from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(board, dir):
    n = len(board)
    price = [[1e9]*n for _ in range(n)]
    price[0][0] = 0
    q = deque([(0,0,0,dir)])
    while q:
        x, y, c, direc = q.popleft()
        if x==n-1 and y==n-1:
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=n or ny<0 or ny>=n or board[nx][ny]==1:
                continue
            if d == direc:
                nc = c + 100
            else:
                nc = c + 600
                
            if nc < price[nx][ny]:
                price[nx][ny] = nc
                q.append((nx, ny, nc, d))
                
    return price[-1][-1]

def solution(board):
    answer = min(bfs(board,0), bfs(board,2))
    return answer