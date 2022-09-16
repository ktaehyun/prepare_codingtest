for t in range(int(input())):
    tc = int(input())
    data = list(map(int, input().split()))
    
    data.sort()
    
    count = 1
    now = 0
    result = data[0]
    for i in range(999):
        if data[i] == data[i+1]:
            count += 1
            if i==998 and now<=count:
                print('#%d'%(t+1), data[i])
                break
            continue
        else:
            if now <= count:
                result = data[i]
                now = count
            count = 1
            
    print('#%d'%(t+1), result)