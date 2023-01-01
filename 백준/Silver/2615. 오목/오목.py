board = [list(map(int, input().split())) for _ in range(19)]

dir = [(0, 1), (-1, 1), (1, 0), (1, 1)]

def check(i, j):
    for d in dir:
        y, x = i+d[0], j+d[1]
        cnt = 1
        while 0 <= y < 19 and x < 19 and board[y][x] == board[i][j]:
            cnt += 1
            y += d[0]
            x += d[1]
            if cnt == 5:
                if not (0<=y<19 and 0<=x<19 and board[y][x] == board[i][j]):
                    if not (0<=i-d[0]<19 and 0<=j-d[1]<19 and board[i-d[0]][j-d[1]]==board[i][j]):
                        print(board[i][j])
                        print(i+1, j+1)
                        exit(0)
                    else:
                        break
                else:
                    break

for j in range(19):
    for i in range(19):
        if board[i][j] != 0:
            check(i, j)

print(0)