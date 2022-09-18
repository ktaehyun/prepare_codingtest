from collections import deque

def solution(priorities, location):
    
    q = deque()
    for i, prio in enumerate(priorities):
        q.append((prio, i))
    
    count = 0
    while q:
        now, index = q.popleft()
        for priority in q:
            if now < priority[0]:
                q.append((now, index))
                break
        else:
            count += 1
            if index == location:
                return count
            
                








# def solution(priorities, location):
    
#     q = []
#     for i in range(len(priorities)):
#         q.append((priorities[i], i))
    
#     result = 0
#     while q:
#         p, index = q.pop(0)
#         for priority in q:
#             if priority[0] > p:
#                 q.append((p, index))
#                 break
#         else:
#             result += 1
#             if index == location:
#                 return result





# from collections import deque

# def solution(priorities, location):
    
#     q = deque()
#     for i in range(len(priorities)):
#         q.append((priorities[i], i))
    
#     count = 0
#     while q:
#         priority, index = q.popleft()
#         for i in range(len(q)):
#             if priority < q[i][0]:
#                 q.append((priority, index))
#                 break
#         else:
#             count += 1
#             if index == location:
#                 return count