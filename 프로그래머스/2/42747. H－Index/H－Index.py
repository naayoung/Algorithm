def solution(citations):
    answer = 0
    citations.sort()
    
    for i in citations:
        count = 0
        for j in citations:
            if j >= i:
                count += 1
        if i >= count:
            if answer < count:
                answer = count
    return answer