def solution(genres, plays):
    answer = []
    
    temp = {}
    for i, gp in enumerate(zip(genres,plays)):
        try:
            temp[gp[0]].append([i, gp[1], temp[gp[0]][-1][2]+gp[1]])
        except:
            temp[gp[0]] = [[i, gp[1], gp[1]]]
            
    temp = dict(sorted(temp.items(), key=lambda x: x[-1][-1][-1], reverse=True))
    for value in temp.values():
        value.sort(key=lambda x: (-x[1], x[0]))
        cnt = 0
        for v in value:
            answer.append(v[0])
            cnt += 1
            if cnt == 2:
                break
                
    return answer