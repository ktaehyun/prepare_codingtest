for tc in range(1, int(input())+1):
    data, K = input().split()
    K = int(K)
    L = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(L):
                for j in range(i+1, L):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now

    print('#{} {}'.format(tc, max(map(int, now))))