import sys
input = sys.stdin.readline
################################################
# 특정 레벨의 최대값을 구하는 함수
def max_level(level):
    if level <= 0:
        return 0

    # 1진 트리의 경우 레벨이 곧 노드
    # 이거 안하면 ZeroDivisionError
    if k == 1:
        return level

    return (k**level - 1) // (k - 1)

################################################
# 자신의 레벨을 찾는 함수
def find_my_level(node):
    i = 1
    while True:
        if max_level(i) >= node:
            return i

        i += 1

################################################
# 자신의 부모노드를 구하는 함수
def find_parent(node, node_level):
    # 루트노드면 -1 출력
    if node == 1:
        return -1

    # 노드가 현재레벨에서 몇번째 수인지 찾기
    my_num_in_level = node - max_level(node_level - 1)

    # 1번부터 시작하므로 0번부터 구하기 위해 -1 한후에 k로 나눈 몫을 구함
    # 그 다음 node_level - 2의 최대값에서 그 몫만큼 더하면 부모노드 -1
    # 따라서 + 1하면 부모노드
    parent = ((my_num_in_level - 1) // k) + max_level(node_level - 2) + 1

    return parent

################################################
# 데이터 입력받기
n, k ,q = map(int, input().split())

for _ in range(q):
    x, y = map(int, input().split())

    if k == 1:
        print(abs(x - y))
        continue

    # 자신의 레벨을 구해줌
    x_level = find_my_level(x)
    y_level = find_my_level(y)

    # 같은 레벨이 될때 까지 레벨 맞추기
    # 그 과정에서 레벨의 차이만큼 거리 추가
    distance = abs(x_level - y_level)
    if x_level > y_level:
        while True:
            if x_level == y_level:
                break

            x = find_parent(x, x_level)
            x_level -= 1

    elif y_level > x_level:
        while True:
            if y_level == x_level:
                break

            y = find_parent(y, y_level)
            y_level -= 1

    # 같은 레벨에서 서로 부모 노드를 찾아가며 거리 2씩 추가
    while True:
        if x == y:
            break

        x = find_parent(x, x_level)
        x_level -= 1
        y = find_parent(y, y_level)
        y_level -= 1
        distance += 2

    # 같아져서 반복 멈추면 거리 출력
    print(distance)