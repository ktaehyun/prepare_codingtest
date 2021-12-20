def solution(N, stages):
    answer = []
    
    stages.sort()
    
    length = len(stages)
    fails = []
    for i in range(1, N+1):
        cnt = stages.count(i)
        if length == 0:
            fail_rate = 0
        else:
            fail_rate = cnt / length
        fails.append((fail_rate, i))
        length -= cnt
    
    fails.sort(key = lambda x: (-x[0], x[1]))
    for j in range(N):
        answer.append(fails[j][1])
        
    return answer