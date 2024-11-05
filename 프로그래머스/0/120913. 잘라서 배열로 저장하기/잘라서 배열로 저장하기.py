def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str)+1, n):
        t = my_str[i:i+n]
        if t != '':
            answer.append(t)
    return answer