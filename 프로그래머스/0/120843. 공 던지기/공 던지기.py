def solution(numbers, k):
    answer = 0
    numbers = numbers*k
    cnt = 0
    for i in range(0, len(numbers), 2):
        cnt += 1
        if cnt == k:
            answer = numbers[i]
            break
        
    return answer