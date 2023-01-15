from itertools import combinations

L, C = map(int, input().split())
words = list(input().split())

check = ['a', 'e', 'i', 'o', 'u']
words.sort()

for word in list(combinations(words, r=L)):
    result = list(word)
    cnt = 0
    for r in result:
        if r in check:
            cnt += 1
            if L-cnt < 2:
                break
    if L-cnt<2 or cnt==0:
        continue
    result = ''.join(result)
    print(result)