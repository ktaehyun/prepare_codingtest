import sys, heapq
input = sys.stdin.readline

def main():
    INF = float('inf')
    for _ in range(int(input())):
        n,cost,m = map(int,input().split())
        dp = [[INF]*(n) for _ in range(cost+1)]
        graph = [[] for i in range(n)]

        for i in range(m):
            u,v,c,d = map(int,input().split())
            u-=1;v-=1
            graph[u].append((v,c,d))

        heap = [(0,0,0)] # dist,cost,node
        while(heap):
            curDist,curCost,curNode = heapq.heappop(heap)
            if curDist > dp[curCost][curNode]:
                continue

            for toNode,toCost,toDist in graph[curNode]:
                d = curDist + toDist
                c = curCost + toCost
                if c <= cost and d < dp[c][toNode]:
                    # 더 높은 cost를 투자할 때의 가중치도 맞춰준다.
                    for i in range(c,cost+1):
                        if dp[i][toNode] > d:
                            dp[i][toNode] = d
                        else:
                            break
                    heapq.heappush(heap,(d,c,toNode))
        print(dp[cost][n-1] if dp[cost][n-1] != INF else "Poor KCM")
main()