from collections import defaultdict

N, d, k, c = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

canEat = defaultdict(int)
cnt = 1
canEat[c] = 1
for i in range(k):
    if canEat[arr[i]] == 0:
        cnt += 1
    canEat[arr[i]] += 1
answer = cnt

for left in range(N):
    right = (left+k)%N
    canEat[arr[left]] -= 1
    if canEat[arr[left]] == 0:
        cnt -= 1
    if canEat[arr[right]] == 0:
        cnt += 1
    canEat[arr[right]] += 1
    answer = max(answer, cnt)
    
print(answer)