from math import ceil

def solution(progresses, speeds):
    answer = [0]
    
    pg = ceil((100-progresses[0])/speeds[0])
    
    for p, s in zip(progresses, speeds):
        if pg >= ceil((100-p)/s):
            answer.append(answer.pop()+1)
        if pg < ceil((100-p)/s):
            answer.append(1)
            pg = ceil((100-p)/s)
            
    return answer