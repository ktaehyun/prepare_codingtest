from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    dg_list = list(permutations(dungeons, len(dungeons)))
    while dg_list:
        now_list = dg_list.pop()
        tmp, cnt = k, 0
        for now in now_list:
            if now[0] > tmp:
                answer = max(answer, cnt)
                break
            else:
                cnt += 1
                tmp -= now[1]
        else:
            answer = max(answer, cnt)
                
    return answer