def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left

# def solution(stones, k):
    
#     cnt, prev, length = 0, 0, max(stones)
#     for i in range(length):
#         now = stones.count(i)
#         prev = now + prev
#         if prev < k:
#             cnt += 1
#         else:
#             for i in range(len(stones)):
#                 stones[i] -= cnt
#             break
            
#     def process(temp):
#         count = 0
#         for i, s in enumerate(stones):
#             if s <= 0:
#                 count += 1
#                 if count == k:
#                     return temp
#             else:
#                 stones[i] -= 1
#                 count = 0
#         return process(temp+1)
        
#     return process(cnt)