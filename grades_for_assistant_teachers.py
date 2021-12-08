from math import ceil

for tc in range(1, int(input())+1):
    # n = 10의 배수
    n, k = map(int, input().split())
    scores = []
    for _ in range(n):
        scores.append(list(map(int, input().split())))
    
    # 총점 = 중간*0.35 + 기말*0.45 + 과제*0.2
    total_score = []
    for i in range(n):
        total_score.append([i+1, scores[i][0]*0.35 + scores[i][1]*0.45 + scores[i][2]*0.2])
        
    total_score.sort(key = lambda x: x[1], reverse=True)
    
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    location = n // 10
    for j in range(n):
        if total_score[j][0] == k:
            index = ceil(len(total_score[:j+1]) / location) - 1
            print('#{} {}'.format(tc, grades[index]))
            break