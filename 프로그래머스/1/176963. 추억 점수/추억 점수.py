def solution(name, yearning, photo):
    answer = []
    for ph in photo:
        temp = 0
        for p in ph:
            if p in name:
                temp += yearning[name.index(p)]
        answer.append(temp)
                
    return answer