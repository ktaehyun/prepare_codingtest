def solution(s):
    ans = len(s)
    
    length = ans
    leng = length // 2
    for i in range(1, leng+1):
        prev, cnt, string = s[:i], 1, ''
        for j in range(i, length, i):
            now = s[j:j+i]
            if now == prev:
                cnt += 1
            else:
                string += (str(cnt) + prev) if cnt>1 else prev
                prev, cnt = now, 1
        string += (str(cnt) + prev) if cnt>1 else prev
        ans = min(ans, len(string))
        
    return ans