def solution(cap, n, deliveries, pickups):
    ans = 0
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    deli, pick = 0, 0
    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]
        while deli>0 or pick>0:
            deli -= cap
            pick -= cap
            ans += (n-i)*2
            
    return ans