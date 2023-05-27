def failure(p):
    tmp = [0] * len(p)

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j-1]

        if p[i] == p[j]:
            j += 1
            tmp[i] = j

    return tmp


while True:
    string = input()

    if string == '.':
        break

    table = failure(string)

    if len(string) % (len(string) - table[-1]) != 0:    # 나머지 확인
        print(1)
    else:
        print(len(string) // (len(string) - table[-1]))