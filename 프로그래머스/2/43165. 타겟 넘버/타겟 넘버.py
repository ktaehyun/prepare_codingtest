def solution(numbers, target):
    
    tmp = numbers.pop(0)
    result = [tmp, -tmp]
    while numbers:
        now = numbers.pop(0)
        temp = []
        while result:
            number = result.pop()
            temp.append(number+now)
            temp.append(number-now)
        result = temp
        
    return result.count(target)