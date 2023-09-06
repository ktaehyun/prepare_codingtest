def solution(m, n, puddles):
    
    puddles = [[q-1,p-1] for [p,q] in puddles]  # 미리 puddles 좌표 거꾸로
    dp = [[0] * m for _ in range(n)]  # dp 초기화
    dp[0][0] = 1  # 시작 위치
    
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue 
            if [i, j] in puddles:  # 웅덩이 위치의 경우 0
                dp[i][j] = 0
            else:  # 현재 칸은 왼쪽 칸, 위 칸의 합산
                # print('\n', dp)
                # print("i-1, j : ", i-1, j)
                # print("i, j-1 : ", i, j-1)
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])
                
    return dp[n-1][m-1] % 1000000007