import re

def solution(my_string):
    answer = 0
    my_string = re.findall(r'\d+',my_string)
    my_string = list(map(int, my_string))
    answer = sum(my_string)
    return answer