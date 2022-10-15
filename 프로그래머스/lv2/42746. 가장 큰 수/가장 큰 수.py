def solution(numbers):
    
    str_numbers = [str(number) for number in numbers]
    sort_numbers = sorted(str_numbers, key = lambda x: (x*4)[:4], reverse=True)
    
    if sort_numbers[0] != '0':
        result = ''.join(sort_numbers)
        return result
    else:
        return '0'