def solution(a, b):
    answer = 0
    num = 2 * a * b
    a, b = str(a), str(b)
    
    if(int(a+b) >= num):
        answer = int(a+b)
    else:
        answer = num
    return answer