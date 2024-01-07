def solution(clothes):
    answer = 1
    dic = {}
    for cloth, value in clothes:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
    for i in dic:
        answer *= dic[i] + 1
    return answer-1