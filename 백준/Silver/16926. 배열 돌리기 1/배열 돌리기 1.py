from collections import deque

N, M, R = map(int, input().split())  # N*M 배열을 반시계로 R번 돌림
arr = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def rotate():
    q = deque()
    for depth in range(min(N, M) // 2):
        r = c = depth

        for dr, dc in move:  # 큐에 담아놓고
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    q.append(arr[r][c])
                    r = nr
                    c = nc
                else:
                    break

        # 돌린다
        for _ in range(R % ((N - depth * 2) * 2 + (M - depth * 2) * 2 - 4)):
            q.appendleft(q.pop())

        for dr, dc in move: #큐에서 돌린 값을 넣는다
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    arr[r][c]=q.popleft()
                    r = nr
                    c = nc
                else:
                    break

# 큐에서 값을 빼 저장한다
rotate()

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()