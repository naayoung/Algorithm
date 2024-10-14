def solution(num_list):
    temp = len(num_list)
    if num_list[temp-1] > num_list[temp-2]:
        t = num_list[temp-1]-num_list[temp-2]
    else:
        t = num_list[temp-1] * 2
    num_list.append(t)
    return num_list