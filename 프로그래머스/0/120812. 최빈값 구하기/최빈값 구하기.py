def solution(array):
    answer = 0
    dict_array = {}
    
    for i in array:
        if i in dict_array:
            dict_array[i] += 1
        else:
            dict_array[i] = 1
    
    max_idx = -1
    max_cnt = 0
    for i in dict_array:
        if dict_array[i] > max_cnt:
            max_cnt = dict_array[i]
            max_idx = i
        elif dict_array[i] == max_cnt:
            max_idx = -1
    
    answer = max_idx
    
    return answer