discounts = [10, 20, 30, 40]
answer = [-1, -1]

def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    discount_list = [0]*m
    
    def search(idx):
        global answer
        if idx == m:
            sale, cost = 0, 0
            for i in range(n):
                tmp = 0
                for j in range(m):
                    if users[i][0] <= discount_list[j]:
                        tmp += emoticons[j] * (100-discount_list[j]) // 100
                if tmp >= users[i][1]:
                    sale += 1
                else:
                    cost += tmp
            if sale>answer[0] or (sale==answer[0] and cost>answer[1]):
                answer = [sale, cost]
            return
        
        for i in range(4):
            discount_list[idx] = discounts[i]
            search(idx+1)
        
    search(0)
    
    return answer