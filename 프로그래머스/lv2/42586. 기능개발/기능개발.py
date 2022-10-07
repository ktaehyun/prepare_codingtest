from math import ceil
from collections import deque

def solution(progresses, speeds):
    
    result = []
    
    queue = deque([ceil((100-progress)/speed)
                        for progress,speed in zip(progresses,speeds)])
    
    prev = queue.popleft()
    count = 1
    while queue:
        now = queue.popleft()
        if prev < now:
            result.append(count)
            count = 1
            prev = now
        else:
            count += 1
    result.append(count)
    
    return result