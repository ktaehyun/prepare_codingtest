import sys
from collections import deque
CHANG_YOUNG, SANG_GEUN = 0, 1
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX_R = 100

R, C = map(int, sys.stdin.readline().rstrip().split())
cave = []
for _ in range(R):
    cave.append(list(sys.stdin.readline().rstrip()))
    # 입력 받으면서 뭔가 할 수 있지 않을까? 
N = int(sys.stdin.readline().rstrip())
H = list(map(int, sys.stdin.readline().rstrip().split()))

# 매번 BFS 돌리는 건 에바고
# 매번 없앨 수 있는 미네랄은 한개
# 그 한개의 상하좌우에 미네랄이 있으면, 그 미네랄 섬이 떨어질 수도 있는 후보.
# 각 미네랄 섬에 대해서 BFS를 했을 때, 섬 중 최저 y 좌표를 구한다. 
# y 좌표가 0이면 break, 0이 아니면 그만큼 떨굼.
# https://chldkato.tistory.com/62

def throw_stick_from_left(h):
    for x in range(C):
        if cave[h][x] == 'x':
            cave[h][x] = '.'
            return h, x
    return -1, -1

def throw_stick_from_right(h):
    for x in range(C-1, -1, -1):
        if cave[h][x] == 'x':
            cave[h][x] = '.'
            return h, x
    return -1, -1

def print_cave():
    for row in cave:
        print(*row, sep='')

def get_cluster_visited(start_y, start_x):
    visited = [[False]*C for _ in range(R)]
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in DIRS:
            ny, nx = y+dy, x+dx
            if not (0 <= ny < R and 0 <= nx < C):
                continue
            if cave[ny][nx] == '.':
                continue
            if visited[ny][nx]:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True
    return visited

def get_min_y_list(visited):
    min_y_list = [-1]*C
    for x in range(C):
        for y in range(R-1, -1, -1):
            if visited[y][x]:
                min_y_list[x] = y
                break
    return min_y_list
            
def get_fall_height(min_y_list):
    min_diff = MAX_R + 1
    for x, min_y in enumerate(min_y_list):
        if min_y == -1: # 엣지 케이스
            continue
        for y in range(min_y + 1, R):
            if cave[y][x] == 'x':
                min_diff = min(min_diff, y - min_y - 1) # 처음 만난 미네랄이 5, min_y가 3이라면 1칸 내릴 수 있음
                break
            if y == R-1: # 바닥
                min_diff = min(min_diff, y - min_y) # 바닥이 5, min_y가 3이라면 2칸 내릴 수 있음
                # break # 어차피 마지막
    return min_diff

def fall(h, visited):
    # 아래서부터 내린다.
    for y in range(R-1, -1, -1):
        for x in range(C):
            if not visited[y][x]:
                continue
            cave[y][x] = '.'
            cave[y+h][x] = 'x'

turn = CHANG_YOUNG
for h in H:
    # 1 -> R-1, 2 -> R-2, ..., R -> 0
    h = R-h
    mineral_y, mineral_x = -1, -1
    if turn == CHANG_YOUNG:
        mineral_y, mineral_x = throw_stick_from_left(h)
        turn = SANG_GEUN
    else:
        mineral_y, mineral_x = throw_stick_from_right(h)
        turn = CHANG_YOUNG
    if (mineral_y, mineral_x) == (-1, -1): # 깨진 미네랄이 없을 때
        continue
    # 후보는, 없어진 미네랄의 상하좌우
    for dy, dx in DIRS:
        ny, nx = mineral_y + dy, mineral_x + dx
        if not (0 <= ny < R and 0 <= nx < C):
            continue
        if cave[ny][nx] == '.':
            continue
        # 주의. 클러스터가 떨어질 때, **그 클러스터 각 열의 맨 아래 부분 중 하나**가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다!
        visited = get_cluster_visited(ny, nx)
        
        # 오답.
        # 맨 아래 층에 있던 애들만 닿는 건 아니다!!!
        # **각 열**의 맨 아래 요소에 대해서 다 체크해야 함. 
        min_y_list = get_min_y_list(visited)
        
        if R-1 in min_y_list: # 바닥에 닿은 맨 아래 요소가 있다면
            continue
                    
        # 최저점이 바닥이 아닌 경우 == 현재 떠 있는 경우
        fall_height = get_fall_height(min_y_list)
        fall(fall_height, visited)

        # 주의. 두 개 이상의 클러스터가 동시에 떨어지는 경우는 없다. 
        break

print_cave()