def solution(m, n, puddles):
    
    puddles = [[q-1,p-1] for [p,q] in puddles]  # 미리 puddles 좌표 거꾸로
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            if [i,j] in puddles:
                dp[i][j] = 0
            elif i==0:
                dp[i][j] = dp[i][j-1]
            elif j==0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
    return dp[n-1][m-1] % 1000000007