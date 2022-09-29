def garo(i):
    c = [0 for _ in range(n)]
    for j in range(n-1):
        if abs(a[i][j] - a[i][j + 1]) > 1:
            return 0

        if a[i][j] < a[i][j + 1]:
            temp = [0 for _ in range(n)]
            for k in range(l):
                if j - k < 0:
                    return 0
                if a[i][j] != a[i][j - k] or c[j - k] != 0:
                    return 0
                temp[j - k] = 1
            c = temp

        elif a[i][j] > a[i][j + 1]:
            temp = [0 for _ in range(n)]
            for k in range(l):
                if j + k + 1 >= n:
                    return 0
                if a[i][j + 1] != a[i][j + k + 1] or c[j + k + 1] != 0:
                    return 0
                temp[j + k + 1] = 1
            c = temp
    return 1


def sero(j):
    c = [0 for _ in range(n)]
    for i in range(n-1):
        if abs(a[i][j] - a[i + 1][j]) > 1:
            return 0

        if a[i][j] < a[i + 1][j]:
            temp = [0 for _ in range(n)]
            for k in range(l):
                if i - k < 0:
                    return 0
                if a[i][j] != a[i - k][j] or c[i - k] != 0:
                    return 0
                temp[i - k] = 1
            c = temp

        elif a[i][j] > a[i + 1][j]:
            temp = [0 for _ in range(n)]
            for k in range(l):
                if i + k + 1 >= n:
                    return 0
                if a[i + 1][j] != a[i + k + 1][j] or c[i + k + 1] != 0:
                    return 0
                temp[i + k + 1] = 1
            c = temp
    return 1


n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    ans += garo(i)
    ans += sero(i)
print(ans)