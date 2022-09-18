def connection(n, computers, cpt, index, network, count):
    while cpt:
        now = cpt.pop(0)
        for i in range(n):
            if network[i]==0 and now[i]==1:
                network[i] = count
                if i != index:
                    cpt.append(computers[i])
                    
    if network.count(0) != 0:
        return connection(n, computers, [computers[network.index(0)]], network.index(0), network, count+1)
    else:
        return count

def solution(n, computers):
    return connection(n, computers, [computers[0]], 0, [0] * n, 1)



# def ntw(id, cnt, n, network, computers):
#     q = [(computers[id], id)]
#     cnt += 1
#     while q:
#         cpt, index = q.pop(0)
#         for i in range(n):
#             if cpt[i] == 1:
#                 if i != index and network[i] == 0:
#                     q.append((computers[i], i))
#                 if network[i] == 0:
#                     network[i] = cnt
#     if network.count(0) == 0:
#         return cnt
#     else:
#         return ntw(network.index(0), cnt, n, network, computers)

# def solution(n, computers):
#     network = [0] * n            
#     cnt = 0
#     return ntw(0, cnt, n, network, computers)