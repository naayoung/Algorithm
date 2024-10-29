def solution(s):
    answer = []
    temp = list(set(s))
    for i in temp:
        cnt = 0
        for j in s:
            if i == j:
                cnt += 1
        if cnt == 1:
            answer.append(i)
    answer.sort()
    answer = ''.join(answer)
    return answer