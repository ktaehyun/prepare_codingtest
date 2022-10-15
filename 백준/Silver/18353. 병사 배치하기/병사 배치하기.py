n = int(input())
data = list(map(int, input().split()))

result = [0] * n

result[0] = 1
for i in range(1, n):
    for j in range(i):
        if data[i] < data[j]:
            result[i] = max(result[i], result[j])
    result[i] += 1

print(n-max(result))