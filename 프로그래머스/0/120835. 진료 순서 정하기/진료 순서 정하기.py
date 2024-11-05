def solution(emergency):
    answer = []
    t = emergency[:]
    t.sort(reverse=True)
    
    for i in emergency:
        temp = t.index(i)+1
        answer.append(temp)
    return answer