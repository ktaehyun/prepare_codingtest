def solution(numbers, target):
    
    q = [-numbers[0], numbers[0]]
    for number in numbers[1:]:
        temp = []
        while q:
            pop_num = q.pop()
            temp.append(pop_num - number)
            temp.append(pop_num + number)
        q = temp
        
    return q.count(target)
