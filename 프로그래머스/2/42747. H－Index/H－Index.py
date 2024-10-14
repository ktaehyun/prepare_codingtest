def solution(citations):
    h_index = 0
    
    for _ in citations:
        h = [citation for citation in citations if citation>=h_index]
        if len(h) >= h_index:
            h_index += 1
        if len(h) < h_index:
            h_index -= 1
            break
            
    return h_index