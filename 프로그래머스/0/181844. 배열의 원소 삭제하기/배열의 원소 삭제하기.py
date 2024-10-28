def solution(arr, delete_list):
    answer = []
    for j in arr:
        if j not in delete_list:
            answer.append(j)
    return answer