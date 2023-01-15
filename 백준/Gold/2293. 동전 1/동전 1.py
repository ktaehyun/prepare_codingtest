n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
    
dp = [0 for i in range(k+1)]  # 사이즈 k+1만큼의 리스트 선언
dp[0] = 1  # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언

for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
            
print(dp[k])