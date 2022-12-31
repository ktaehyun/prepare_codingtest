import heapq

n, m = map(int, input().split())
data = list(map(int, input().split()))
q = []
for i in range(n):
  heapq.heappush(q, data[i])
 
for i in range(m):
  x = heapq.heappop(q)
  y = heapq.heappop(q)
  heapq.heappush(q, x+y)
  heapq.heappush(q, x+y)
 
print(sum(q))