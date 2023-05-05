from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

r,c,k = map(int, input().split())
temperature = [[[0,0,0] for _ in range(c)] for _ in range(r)]
visited = [[0]*c for _ in range(r)]
visited_num = 0

targets = []
heaters = []
for x in range(r):
    tmp = list(map(int, input().split()))
    for y in range(c):
        if tmp[y] == 5:
            targets.append((x,y))
        elif tmp[y] > 0:
            if tmp[y] == 1:
                typ = 1
            elif tmp[y] == 2:
                typ = 3
            elif tmp[y] == 3:
                typ = 0
            else:
                typ = 2
            heaters.append((x,y,typ))

w = int(input())
wall_board = [[[False]*4 for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x,y,t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall_board[x][y][0] = wall_board[x-1][y][2] = True
    else:
        wall_board[x][y][1] = wall_board[x][y+1][3] = True

def solv():
    answer = 0
    while True:
        spread_heat()
        set_temperature()
        answer += 1
        if check_targets():
            print(answer)
            return
        if answer == 100:
            print(101)
            return

def check_targets():
    for x,y in targets:
        if temperature[x][y][0] < k:
            return False
    return True
def set_temperature():
    global temperature

    for x in range(r):
        for y in range(c):
            if temperature[x][y][0] == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if point_validator(nx,ny,(d+2)%4,False) and temperature[x][y][0] > temperature[nx][ny][0]:
                    temperature[nx][ny][1] += (temperature[x][y][0]-temperature[nx][ny][0])//4
                    temperature[x][y][2] += (temperature[x][y][0]-temperature[nx][ny][0])//4

    for x in range(r):
        for y in range(c):
            temperature[x][y][0] += temperature[x][y][1]-temperature[x][y][2]
            temperature[x][y][1] = temperature[x][y][2] = 0

    for x in range(r):
        for y in range(c):
            if x == 0 or y == 0 or x == r-1 or y == c-1:
                if temperature[x][y][0] > 0:
                    temperature[x][y][0] -= 1
def spread_heat():
    global temperature,visited,visited_num

    for sx,sy,typ in heaters:
        visited_num += 1
        sx += dx[typ]
        sy += dy[typ]

        q = deque([(sx,sy)])
        visited[sx][sy] = visited_num

        temperature[sx][sy][0] += 5

        for amount in range(4,0,-1):
            if not q:
                break
            q_len = len(q)
            for idx in range(q_len):
                x,y = q.pop()
                nx = x + dx[typ] + dx[(typ-1)%4]
                ny = y + dy[typ] + dy[(typ-1)%4]
                if point_validator(nx,ny,(typ+2)%4) and not wall_board[x][y][(typ-1)%4]:
                    temperature[nx][ny][0] += amount
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))

                nx = x + dx[typ]
                ny = y + dy[typ]
                if point_validator(nx,ny,(typ+2)%4):
                    temperature[nx][ny][0] += amount
                    visited[nx][ny] = visited_num
                    q.appendleft((nx, ny))

                nx = x + dx[typ] + dx[(typ+1)%4]
                ny = y + dy[typ] + dy[(typ+1)%4]
                if point_validator(nx,ny,(typ+2)%4) and not wall_board[x][y][(typ+1)%4]:
                    temperature[nx][ny][0] += amount
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))

def point_validator(x,y,typ,flag=True):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif wall_board[x][y][typ]:
        return False
    elif flag and visited[x][y] == visited_num:
        return False
    return True

solv()