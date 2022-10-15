def solution(N, stages):
    
    answer = []
    
    stages.sort()
    
    result = []
    for n in range(1, N+1):
        if n in stages:
            fail_rate = stages.count(n) / len(stages[stages.index(n):])
            result.append((fail_rate, n))
        else:
            fail_rate = 0
            result.append((fail_rate, n))
        
    result.sort(key = lambda x: (-x[0], x[1]))
    for rs in result:
        answer.append(rs[1])
    
    return answer