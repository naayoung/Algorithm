def solution(num_list):
    answer = 0
    a, b = '', ''
    for n in range(len(num_list)):
        if num_list[n]%2 == 0:
            b += str(num_list[n])
        else:
            a += str(num_list[n])
    answer = int(a) + int(b)
    return answer