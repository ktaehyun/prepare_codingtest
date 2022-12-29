from collections import deque


def bfs():
    q = deque([S])
    visited = [0] * (F + 1)
    visited[S] = 1
    while q:
        c = q.popleft()
        if c == G:
            print(visited[G] - 1)
            return

        up = c + U
        down = c - D
        if up <= F and not visited[up]:
            q.append(up)
            visited[up] = visited[c] + 1
        if down > 0 and not visited[down]:
            q.append(down)
            visited[down] = visited[c] + 1

    else:
        print('use the stairs')
        return


if __name__ == '__main__':
    F, S, G, U, D = map(int, input().split())
    # F: 건물 층수, S: 강호 위치, G: 회사 위치
    bfs()