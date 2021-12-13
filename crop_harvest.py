for tc in range(1, int(input())+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
        
    int_arr = []
    for i in range(n):
        int_arr.append([int(arr[i][j]) for j in range(n)])
        
    mid_index = n // 2
    result = 0
    for i in range(mid_index):
        result += (sum(int_arr[i][mid_index-i:mid_index+i+1]) + sum(int_arr[n-1-i][mid_index-i:mid_index+i+1]))
    result += sum(int_arr[mid_index])
    
    print('#{} {}'.format(tc, result))