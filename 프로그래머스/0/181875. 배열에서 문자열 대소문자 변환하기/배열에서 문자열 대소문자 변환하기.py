def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i%2 == 0:
            temp = strArr[i].lower()
        else:
            temp = strArr[i].upper()
        answer.append(temp)
    return answer