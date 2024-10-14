def solution(str_list, ex):
    temp = []
    answer = ''
    for s in str_list:
        if ex not in s:
            temp.append(s)
    answer = ''.join(temp)
    return answer