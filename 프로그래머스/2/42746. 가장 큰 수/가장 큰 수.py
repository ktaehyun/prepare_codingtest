def solution(numbers):
    
    str_num = [str(number) for number in numbers]
    sort_num = sorted(str_num, key=lambda x: (x*4)[:4], reverse=True)
    
    if sort_num[0] != '0':
        return ''.join(sort_num)
    return '0'