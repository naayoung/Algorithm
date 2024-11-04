def solution(arr, queries):
    answer = []
    for q in queries:
        a, b = q[0], q[1]
        arr[a], arr[b] = arr[b], arr[a]
    answer = arr
    return answer