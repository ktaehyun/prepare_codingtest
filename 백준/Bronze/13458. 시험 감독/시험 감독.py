n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())

result = len(A)
for a in A:
    a -= b
    if a > 0:
        if a % c:
            result += (a//c) + 1
        else:
            result += a//c
            
print(result)