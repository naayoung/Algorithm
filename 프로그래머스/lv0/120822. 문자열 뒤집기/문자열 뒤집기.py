def solution(my_string):
    my_string = list(map(str, my_string))
    my_string.reverse()
    answer = ''.join(my_string)
    return answer