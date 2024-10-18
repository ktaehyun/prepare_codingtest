def solution(n, s, a, b, fares):
    ans = 1e9
    cost = [[1e9]*(n+1) for _ in range(n+1)]
    
    for i,j,c in fares:
        cost[i][j] = c
        cost[j][i] = c
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = min(cost[i][j], cost[i][k]+cost[j][k])
                        
    for i in range(1, n+1):
        ans = min(cost[s][i]+cost[i][a]+cost[i][b], ans)
    return ans