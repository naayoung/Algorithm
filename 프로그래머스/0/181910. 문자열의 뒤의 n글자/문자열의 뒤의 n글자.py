def solution(my_string, n):
    answer = ''
    temp = len(my_string)
    answer = my_string[temp-n:]
    return answer