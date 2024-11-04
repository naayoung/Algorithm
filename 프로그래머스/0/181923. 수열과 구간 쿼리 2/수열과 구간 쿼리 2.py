def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = 1000000
        for i in range(s, e+1):
            if arr[i] > k:
                temp = min(temp, arr[i])
        if temp == 1000000:
            temp = -1
        answer.append(temp)
                
    return answer