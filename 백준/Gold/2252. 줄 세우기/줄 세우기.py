from collections import deque

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)] #인접리스트
indegree=[0]*(N+1)

queue=deque()
result=[]

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1 #진입차수 구하기

def topologicalSort(): #bfs로 구현
    for i in range(1,N+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        V=queue.popleft()
        result.append(V)
        for i in graph[V]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)

topologicalSort()
for num in result:
    print(num, end=' ')