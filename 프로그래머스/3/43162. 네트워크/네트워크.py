def connection(n, computers, cpt, index, network, count):
    
    while cpt:
        now = cpt.pop(0)
        for i in range(n):
            if network[i]==0 and now[i]==1:
                network[i] = count
                if i != index:
                    cpt.append(computers[i])
                    
    if network.count(0) != 0:
        # print(network)
        return connection(n, computers, [computers[network.index(0)]], network.index(0), network, count+1)
    else:
        # print(network)
        return count

def solution(n, computers):
    
    return connection(n, computers, [computers[0]], 0, [0]*n, 1)