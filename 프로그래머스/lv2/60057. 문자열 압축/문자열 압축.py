def solution(s):
    
    result = len(s)
    
    length = result
    for i in range(1, len(s)//2+1):
        temp, prev, cnt = '', s[:i], 1
        for j in range(i, length, i):
            now = s[j:j+i]
            if prev == now:
                cnt += 1
            else:
                temp += (str(cnt) + prev) if cnt!=1 else prev
                prev, cnt = now, 1
        temp += (str(cnt) + prev) if cnt!=1 else prev
        result = min(result, len(temp))
        
    return result