def solution(my_string, s, e):
    answer = ''
    temp = my_string[s:e+1]
    temp = temp[::-1]

    for n in range(s):
        answer += my_string[n]
    answer += temp
    for n in range(e+1, len(my_string)):
        answer += my_string[n]
    return answer