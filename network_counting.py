def ntw(id, cnt, n, network, computers):
    q = [(computers[id], id)]
    cnt += 1
    while q:
        cpt, index = q.pop(0)
        for i in range(n):
            if cpt[i] == 1:
                if i != index and network[i] == 0:
                    q.append((computers[i], i))
                if network[i] == 0:
                    network[i] = cnt
    if network.count(0) == 0:
        return cnt
    else:
        return ntw(network.index(0), cnt, n, network, computers)

def solution(n, computers):
    network = [0] * n            
    cnt = 0
    return ntw(0, cnt, n, network, computers)