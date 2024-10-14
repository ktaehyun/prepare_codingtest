def solution(s):
    
    cnt = 0
    for now in s:
        if now == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    return False