from math import ceil

def solution(progresses, speeds):
    
    days = [ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]
    
    result, now_day, count = [], days[0], 1
    for i in range(1, len(days)):
        if days[i] > now_day:
            now_day = days[i]
            result.append(count)
            count = 1
        else:
            count += 1
    result.append(count)
    
    return result
    

# from math import ceil

# def solution(progresses, speeds):
#     answer = [0]
    
#     pg = ceil((100-progresses[0])/speeds[0])
    
#     for p, s in zip(progresses, speeds):
#         if pg >= ceil((100-p)/s):
#             answer.append(answer.pop()+1)
#         if pg < ceil((100-p)/s):
#             answer.append(1)
#             pg = ceil((100-p)/s)
            
#     return answer