def solution(brown, yellow):
    for a in range(3, brown):
        for b in range(3, a+1):
            if brown==2*(a+b-2) and yellow==(a*b)-brown:
                result = [a, b]
                break
    return result