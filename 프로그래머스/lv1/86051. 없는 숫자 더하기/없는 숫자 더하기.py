def solution(numbers):
    answer = []
    
    for i in range(0, 10):
        answer.append(i)
    
    for i in numbers:
        answer.remove(i)
        
    answer = sum(answer)
    return answer