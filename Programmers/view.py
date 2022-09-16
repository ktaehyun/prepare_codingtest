for tc in range(10):
    le = int(input())
    buildings = list(map(int, input().split()))
    
    get_sum = 0
    count = 2
    for i in range(2, le-2):
        if count==0 or count==1:
            count += 1
            continue
        get_max = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])
        if buildings[i] > get_max:
            get_sum += buildings[i] - get_max
            count = 0
                
    print('#{} {}'.format(tc+1, get_sum))