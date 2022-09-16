for tc in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))
    
    for _ in range(dump):
        max_h, max_id = max(heights), heights.index(max(heights))
        min_h, min_id = min(heights), heights.index(min(heights))
        result = max_h - min_h
        if result==0 or result==1:
            break
        heights[max_id] -= 1
        heights[min_id] += 1
        
    print('#{} {}'.format(tc, max(heights) - min(heights)))