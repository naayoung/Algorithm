def solution(left, right):
    answer = 0
    
    for j in range(left, right+1):
        count = 0
        for i in range(1, j+1):
            if(j%i == 0):
                count += 1
        if(count%2 == 0):
            answer += j
        else:
            answer -= j
    return answer