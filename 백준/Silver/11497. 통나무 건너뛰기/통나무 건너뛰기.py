T=int(input())

for i in range(T):
    N=int(input())
    trees=list(map(int,input().split()))
    trees.sort()
    result=0
    for j in range(2, N):
        result=max(result,abs(trees[j]-trees[j-2]))
        
    print(result)