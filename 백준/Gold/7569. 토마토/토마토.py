from collections import deque


M, N, H = map(int, input().split())
# boxes[h][x][y]
now = deque([])
boxes = [[] for _ in range(H)]
check = 0
for h in range(H):
    temp = []
    for n in range(N):
        temp = list(map(int, input().split()))
        boxes[h].append(temp)
        for m, tmp in enumerate(temp):
            if tmp == 1:
                now.append((h, n, m))
            elif check==0 and tmp==0:
                check = 1

                
if check==0 and now!=deque([]):
    print(0)
else:
    def progress(now, temp=[], days=0):
        # d = [동, 서, 남, 북, 위, 아래]
        dh = [0, 0, 0, 0, -1, 1]
        dx = [0, 0, 1, -1, 0, 0]
        dy = [1, -1, 0, 0, 0, 0]
        while now:
            h, x, y = now.popleft()
            for d in range(6):
                nh = h + dh[d]
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nh<H and 0<=nx<N and 0<=ny<M and boxes[nh][nx][ny]==0:
                    boxes[nh][nx][ny] = 1
                    temp.append((nh, nx, ny))
            if now == deque([]):
                days += 1
                now, temp = deque(temp), []

        for box in boxes:
            for b in box:
                if b.count(0) != 0:
                    return -1

        return days-1

    print(progress(now))