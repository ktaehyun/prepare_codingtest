from collections import deque

def solution(priorities, location):
    
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    count = 0
    while q:
        p, index = q.popleft()
        for i in range(len(q)):
            if p < q[i][0]:
                q.append((p, index))
                break
        else:
            count += 1
            if index == location:
                return count