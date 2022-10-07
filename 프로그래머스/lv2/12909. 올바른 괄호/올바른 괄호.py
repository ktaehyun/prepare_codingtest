from collections import deque

def solution(s):
    
    answer = True
    
    queue = deque(s)
    check = 0    
    while queue:
        gwalho = queue.popleft()
        
        if gwalho == "(" :
            check += 1
        else:
            check -= 1
            
        if check < 0 :
            answer = False
            break
            
    if check > 0 :
        answer = False
        
    return answer