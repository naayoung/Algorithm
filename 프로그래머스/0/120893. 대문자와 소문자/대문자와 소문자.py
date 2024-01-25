def solution(my_string):
    answer = []
    my_string = list(map(str, my_string))
    for i in my_string:
        if i.islower():
            temp = i.upper()
            answer.append(temp)
        else:
            temp = i.lower()
            answer.append(temp)
    return "".join(answer)