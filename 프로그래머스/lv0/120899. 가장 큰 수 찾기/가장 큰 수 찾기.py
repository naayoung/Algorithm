def solution(array):
    max_array = max(array)
    max_index = array.index(max_array)
    answer = [max_array, max_index]
    return answer