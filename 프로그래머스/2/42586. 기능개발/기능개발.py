from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque([ceil((100-progress)/speed) for progress,speed in zip(progresses,speeds)])
    prev = q.popleft()
    count = 1
    while q:
        now = q.popleft()
        if prev < now:
            answer.append(count)
            count = 1
            prev = now
        else:
            count += 1
    answer.append(count)
    
    return answer