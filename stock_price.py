from collections import deque

def solution(prices):
    answer = []
    
    q = deque(prices)
    while q:
        time = 0
        price = q.popleft()
        if q == deque([]):
            answer.append(0)
            break
        for x in q:
            time += 1
            if x < price:
                answer.append(time)
                break                    
        else:
            answer.append(time)
    
    return answer
