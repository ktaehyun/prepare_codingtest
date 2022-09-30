def distance(chicken): # 거리를 계산하는 함수
    dist = 0
    for r1, c1 in home:
        dist += min([(abs(r1-r2) + abs(c1-c2)) for r2, c2 in chicken])
    return dist

def dfs(L, cur): # 조합을 만들어 치킨 거리의 최솟값을 찾는 함수
    global min_dist
    if L == M:
        select_chicken = [chicken[i] for i in range(chicken_len) if visited[i]]
        min_dist = min(min_dist, distance(select_chicken))
        return
    
    for i in range(cur, chicken_len):
        if visited[i] == 0:
            visited[i] = 1
            dfs(L + 1, i + 1)
            visited[i] = 0

N, M = map(int, input().split()) # 도시 크기, 치킨집 개수
city = [] # 도시
chicken = [] # 치킨집
home = [] # 집

for r in range(N):
    temp = list(map(int, input().split()))
    city.append(temp) # 도시의 각 행에 대한 정보 추가
    for c in range(N):
        if temp[c] == 2: # 치킨집인 경우
            chicken.append((r,c))
        elif temp[c] == 1: # 집인 경우
            home.append((r,c))
    
if len(chicken) == M: # 이미 M개이므로 치킨집을 폐업시킬 필요가 없음
    print(distance(chicken))
else: # M개씩 조합을 만들어 도시의 치킨 거리의 최솟값을 찾아야 함
    min_dist = 9000000000 # 대략적인 큰 수로 도시의 치킨 거리 초기화
    chicken_len = len(chicken)
    visited = [0] * chicken_len
    dfs(0, 0)
    print(min_dist)