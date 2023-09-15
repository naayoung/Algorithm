def solution(num, total):
    answer = []
    if(total%num == 0):
        mid = total // num
    else:
        mid = total//num+1
    first = mid - num//2
    
    for i in range(first, first+num):
        answer.append(i)
    return answer