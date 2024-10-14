def solution(t, p):
    answer = 0
    temp = []
    for i in range(len(t)):
        tt = t[i:i+len(p)]
        if len(tt) == len(p):
            temp.append(tt)
    for i in temp:
        if i <= p:
            answer += 1
    return answer