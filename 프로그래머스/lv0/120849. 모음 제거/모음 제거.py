def solution(my_string):
    gather = ["a", "e", "i", "o", "u"]
    my_string = list(map(str, my_string))
    my_string = [i for i in my_string if i not in gather]
    answer = ''.join(my_string)
    return answer