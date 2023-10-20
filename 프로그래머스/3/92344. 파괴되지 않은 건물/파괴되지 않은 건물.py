def solution(board, skill):
    answer = 0
    m, n = len(board), len(board[0])
    acc = [ ([0]*(n+1)) for _ in range(m+1)]

    # 면적을 한번에 계산하기 위해 각 끝의 4개의 좌표만 표시해 둠
    for s in skill:
        types = 0
        if s[0] == 1: types = -1
        elif s[0] == 2 : types = 1
        startY, startX, endY, endX = s[1], s[2], s[3], s[4]
        degree = s[5]

        acc[startY][startX] += degree*types
        acc[startY][endX+1] -= degree*types
        acc[endY+1][startX] -= degree*types
        acc[endY+1][endX+1] += degree*types

    # 누적값 계산 (acc 값 x행 방향으로 채우기)
    for j in range(m):
        for i in range(1, n):
            acc[j][i] += acc[j][i-1]

    # 방금 계산한 x 행 acc 값을 토대로 acc값 y열 방향으로 채우기
    for i in range(n):
        for j in range(1,m):
            acc[j][i] += acc[j-1][i]

    # board에 acc값 반영
    for j in range(m):
        for i in range(n):    
            board[j][i] += acc[j][i]
            if board[j][i] > 0:
                answer += 1

    return answer