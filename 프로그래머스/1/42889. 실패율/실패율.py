def solution(N, stages):
    ans = []
    
    stages.sort()
    result = []
    for n in range(1, N+1):
        if n in stages:
            fail_rate = stages.count(n) / len(stages[stages.index(n):])
            result.append((fail_rate, n))
        else:
            result.append((0, n))
            
    result.sort(key=lambda x: (-x[0], x[1]))
    for rs in result:
        ans.append(rs[1])
        
    return ans