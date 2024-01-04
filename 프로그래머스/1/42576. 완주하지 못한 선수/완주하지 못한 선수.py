def solution(participant, completion):
    temp = {}
    for part in participant:
        if part in temp:
            temp[part] += 1
        else:
            temp[part] = 1
    for com in completion:
        if temp[com] == 1:
            del temp[com]
        else:
            temp[com] -= 1
    answer = list(temp.keys())[0]
    return answer