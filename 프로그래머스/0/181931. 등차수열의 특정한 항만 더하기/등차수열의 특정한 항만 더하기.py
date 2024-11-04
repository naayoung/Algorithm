def solution(a, d, included):
    answer = 0
    temp = a
    for i in range(len(included)):
        if included[i]:
            answer += temp
        temp += d

    return answer