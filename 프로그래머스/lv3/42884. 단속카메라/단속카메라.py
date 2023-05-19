def solution(routes):
    
    answer = 1
    routes.sort(key=lambda x: x[1])
    prev = routes.pop(0)
    while routes:
        now = routes.pop(0)
        if prev[1] >= now[0]:
            continue
        else:
            answer += 1
            prev = now
            
    return answer