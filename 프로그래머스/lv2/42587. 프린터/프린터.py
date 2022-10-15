from collections import deque

def solution(priorities, location):
    
    q = deque()
    for i, prio in enumerate(priorities):
        q.append((prio, i))
    
    count = 0
    while q:
        now, index = q.popleft()
        for priority in q:
            if now < priority[0]:
                q.append((now, index))
                break
        else:
            count += 1
            if index == location:
                return count