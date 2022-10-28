from collections import deque
    
def checking(target, words, q, length, moment, time):
    time += 1
    count, temp = 0, []
    while q:
        now = q.popleft()
        if now == target:
            return time
        for word in words:
            for i in range(length):
                if word in moment:
                    break
                elif now[i]==word[i]:
                    count += 1
            if count == length - 1:
                temp.append(word)
                moment.append(word)
            else:
                count = 0
    return checking(target, words, deque(temp), length, moment, time)

def solution(begin, target, words):
    filter_words = list(filter(lambda x: target in x, words))
    if len(filter_words) == 0:
        return 0
    q, count, length = deque(), 0, len(begin)
    for word in words:
        for i in range(length):
            if begin[i] == word[i]:
                count += 1
        if count == length - 1:
            q.append(word)
        else:
            count = 0
    return checking(target, words, q, length, list(q), 0)