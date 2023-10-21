def solution(s):
    ans = len(s)
    
    length = ans
    point = length//2
    for end in range(1, point+1):
        prev, cnt, string = s[:end], 1, ''
        for i in range(end, length+1, end):
            now = s[i:i+end]
            if now == prev:
                cnt += 1
            else:
                string += (str(cnt) + prev) if cnt>1 else prev
                prev, cnt = now, 1
        string += (str(cnt) + prev) if cnt>1 else prev
        ans = min(ans, len(string))
        
    return ans