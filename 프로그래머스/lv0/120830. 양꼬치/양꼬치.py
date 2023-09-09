def solution(n, k):
    if(n//10 >= 1):
         answer = n * 12000 + (k-n//10) * 2000
    else:
        answer = n * 12000 + k * 2000
    return answer