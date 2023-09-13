def solution(i, j, k):
    answer = 0
    k = str(k)
    
    arr = list(map(str, range(i, j+1)))
    arr_new = "".join(arr)
    answer = arr_new.count(k)
    
    return answer