n = int(input())
for x in range(1, n+1):
    str_x = str(x)
    sum_count = str_x.count('3') + str_x.count('6') + str_x.count('9')
    if sum_count >= 1:
        print('-' * sum_count, end=' ')
        continue
    else:
        print(x, end=' ')
