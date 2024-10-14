from collections import deque

def solution(priorities, location):
    
    q = deque()
    for i, prio in enumerate(priorities):
        q.append((i, prio))
        
    count = 0
    while q:
        idx, now = q.popleft()
        for priority in q:
            if now < priority[1]:
                q.append((idx, now))
                break
        else:
            count += 1
            if idx == location:
                return count