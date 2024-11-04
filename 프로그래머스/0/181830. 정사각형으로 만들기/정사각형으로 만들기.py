def solution(arr):
    answer = []
    temp = len(arr)
    temp1 = len(arr[0])
    
    if temp == temp1:
        answer = arr
    if temp > temp1:
        for i in range(temp):
            t = arr[i]
            for _ in range(temp-temp1):
                t.append(0)
            answer.append(t)
    if temp < temp1:
        answer = arr
        for _ in range(temp1-temp):
            answer.append([0]*temp1)
    return answer