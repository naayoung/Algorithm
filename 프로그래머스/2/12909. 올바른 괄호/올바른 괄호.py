def solution(s):
    answer = True
    temp = []
    
    for i in s:
        if len(temp) == 0:
            temp.append(i)
        elif temp[-1] == "(" and i == ")":
            temp.pop()
        else:
            temp.append(i)
    
    if len(temp) != 0:
        answer = False

    return answer