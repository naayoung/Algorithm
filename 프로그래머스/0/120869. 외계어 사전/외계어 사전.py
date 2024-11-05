def solution(spell, dic):
    answer = 0
    
    t = 0
    for i in dic:
        temp = 0
        for j in spell:
            if j in i:
                temp += 1
        if temp == len(spell):
            t += 1
    if t == 0:
        answer = 2
    else:
        answer = 1
    return answer