def solution(my_string, letter):
    my_string = list(map(str, my_string))
    while(letter in my_string):
        my_string.remove(letter)
    answer = ''.join(my_string)
    return answer