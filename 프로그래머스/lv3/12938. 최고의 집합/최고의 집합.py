def solution(n, s):
    
    if s // n < 1:
        return [-1]
    
    elif s % n != 0:
        rest = s % n
        value = s // n
        answer = [ value for _ in range(n) ]
        for i in range(n-1, n-1-rest, -1):
            answer[i] += 1
            
    else:
        value = s // n
        answer = [ value for _ in range(n) ]
        
    return answer