def solution(answers):
    
    answer = []
    
    std1 = [1,2,3,4,5] * 2000
    std2 = [2,1,2,3,2,4,2,5] * 1250
    std3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if std1[i] == answers[i]:
            count1 += 1
        if std2[i] == answers[i]:
            count2 += 1
        if std3[i] == answers[i]:
            count3 += 1
    
    result = []
    result.append([count1, 1])
    result.append([count2, 2])
    result.append([count3, 3])
    result.sort(key=lambda x: (-x[0], x[1]))
    for i in range(3):
        if result[i][0] == result[0][0]:
            answer.append(result[i][1])
        else:
            break
            
    return answer