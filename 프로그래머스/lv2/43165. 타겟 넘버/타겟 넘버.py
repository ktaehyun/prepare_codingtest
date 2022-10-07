def solution(numbers, target):
    
    q = [numbers[0], -numbers[0]]
    for number in numbers[1:]:
        temp = []
        while q:
            now = q.pop()
            temp.append(now + number)
            temp.append(now - number)
        q = temp
        
    return q.count(target)