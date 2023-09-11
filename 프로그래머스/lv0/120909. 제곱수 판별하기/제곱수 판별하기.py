def solution(n):
    answer = 0
    
    if(n%(n**0.5)==0):
        answer = 1
    else:
        answer = 2  
    return answer