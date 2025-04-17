def solution(array, commands):
    ans = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        tmp = array[i-1:j]
        tmp.sort()
        ans.append(tmp[k-1])
        
    return ans