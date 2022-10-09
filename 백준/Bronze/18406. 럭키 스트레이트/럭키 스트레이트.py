n = str(input())

half = len(n)//2
left, right = 0, 0
for i in range(half):
    left += int(n[i])
    right += int(n[i+half])

result = 'READY'
if left == right:
    result = 'LUCKY'

print(result)