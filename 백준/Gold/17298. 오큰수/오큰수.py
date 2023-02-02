from collections import deque

n = int(input())
seq = list(map(int, input().split()))

oh_big = [-1] * n
stack = deque()

for i in range(n):
    while stack and (stack[-1][0] < seq[i]):
        tmp, idx = stack.pop()
        oh_big[idx] = seq[i]
    stack.append([seq[i], i])

print(*oh_big)