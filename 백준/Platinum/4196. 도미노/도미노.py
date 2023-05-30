import sys
ssr = sys.stdin.readline

def find_scc(graph, inv_graph, N):
    def init_dfs(node):
        inner_stack = [node]
        while inner_stack:
            node = inner_stack[-1]
            visited[node] = True
            have_child_node = False
            for child_node in graph[node]:
                if not visited[child_node]:
                    inner_stack.append(child_node)
                    have_child_node = True
                    visited[child_node] = True
                    break
            if not have_child_node:
                stack.append(inner_stack.pop())


    visited = [False for _ in range(N + 1)]
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:
            init_dfs(i)

    def find_scc(node, scc_num):
        inner_stack = [node]
        while inner_stack:
            node = inner_stack[-1]
            visited[node] = True
            have_child_node = False
            for child_node in inv_graph[node]:
                if not visited[child_node]:
                    inner_stack.append(child_node)
                    have_child_node = True
                    visited[child_node] = True
                    break
            if not have_child_node:
                scc[node] = scc_num
                inner_stack.pop()

    scc = [0 for _ in range(N + 1)]
    scc_num = 1

    for i in range(N + 1): visited[i] = False
    for i in range(1, N + 1):
        node = stack.pop()
        if not visited[node]:
            find_scc(node, scc_num)
            scc_num += 1
    scc_num -= 1
    scc_map = [[] for _ in range(scc_num + 1)]
    for node in range(1, N + 1):
        for child_node in inv_graph[node]:
            if scc[node] != scc[child_node] and scc[child_node] not in scc_map[scc[node]]:
                scc_map[scc[node]].append(scc[child_node])
    return scc, scc_map, scc_num

T = int(ssr())
for _ in range(T):
    N, M = map(int, ssr().split())
    graph = [[] for _ in range(N + 1)]
    inv_graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        t1, t2 = map(int, ssr().split())
        graph[t1].append(t2)
        inv_graph[t2].append(t1)
    scc, scc_map, num_scc = find_scc(graph, inv_graph, N)
    ans = 0
    for i in range(1, num_scc + 1):
        if not scc_map[i]:
            ans += 1
    print(ans)