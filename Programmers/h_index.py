def solution(citations):
    h = 0
    
    for i in citations:
        h_index = [citation for citation in citations if citation >= h]
        if len(h_index) >= h:
            h += 1
        if len(h_index) < h:
            h -= 1
            break
            
    return h