from collections import deque

def solution(prices):
    answer = []
    
    q = deque()
    for price in prices:
        q.append(price)
    
    while q:
        time = 0
        price = q.popleft()
        if q == deque([]):
            answer.append(0)
            break
        for x in q:
            time += 1
            if x >= price:
                if time == len(q):
                    answer.append(time)
            else:
                answer.append(time)
                break
    
    return answer