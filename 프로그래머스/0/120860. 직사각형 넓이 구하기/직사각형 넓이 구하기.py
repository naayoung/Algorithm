def solution(dots):
    answer = 0
    mid = min(dots)
    mad = max(dots)
    
    answer = (mad[0]-mid[0])*(mad[1]-mid[1])
    return answer