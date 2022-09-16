for t in range(1, int(input())+1):
    num = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr)-1, -1, -1):
        if last > arr[i]:
            cnt += last - arr[i]
        else:
            last = arr[i]
    print("#{} {}".format(t, cnt))