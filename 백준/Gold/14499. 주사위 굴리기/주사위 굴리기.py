# r,c = x,y

# 위:1 / 동:3

# 처음 모두 0

# 바닥면이 0 이면, 바닥의 숫자가 주사위로

# n,m = 세로,가로

# 명령수 k

# 동1 / 서2 / 북3 / 남4 (+1)

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

# [ 북0 위1 남2 하3 서4 동5 ]
dice = list(0 for _ in range(6))

# d = [동,서,북,남]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 동-> 3>4>1>5>3 / 서-> 3>5>1>4>3 / 북-> 0>3>2>1>0 / 남-> 3>0>1>2>3

def progress(d, r, c):
    
    global dice, maps
    
    if d==0: #동
        dice[3],dice[4],dice[1],dice[5] = dice[4],dice[1],dice[5],dice[3]
    elif d==1: #서
        dice[3],dice[5],dice[1],dice[4] = dice[5],dice[1],dice[4],dice[3]
    elif d==2: #북
        dice[0],dice[3],dice[2],dice[1] = dice[3],dice[2],dice[1],dice[0]
    else: #남
        dice[3],dice[0],dice[1],dice[2] = dice[0],dice[1],dice[2],dice[3]
        
    if maps[r][c] == 0:
        maps[r][c] = dice[3]
    else:
        dice[3] = maps[r][c]
        maps[r][c] = 0

while order:
    direction = order.pop(0) - 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if 0<=nx<n and 0<=ny<m:
        progress(direction, nx, ny)
        x,y = nx,ny
        print(dice[1])