x,y = map(int,input().split())
array = []
n = int(input())
for _ in range(n+1):
    position, value = map(int,input().split())
    if position == 1:
        array.append(y+value)
    elif position == 2:
        array.append(-value)
    elif position == 3:
        array.append(y-value)
    else:
        array.append(-x-y+value)

total = 2*x+2*y
cnt = 0
for i in range(n):
    val = array[n] - array[i]
    if val<0:
        val *= -1
    if total - val > val:
        cnt += val
    else:
        cnt += (total-val)
        
print(cnt)