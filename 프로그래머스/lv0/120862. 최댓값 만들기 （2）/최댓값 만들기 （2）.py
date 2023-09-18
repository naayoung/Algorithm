def solution(numbers):
    answer = 0
    
    """배열 정렬"""
    numbers.sort()
    
    """음수의 곱을 고려하여 배열의 오른쪽에서 2개 값과 왼쪽에서 2개 값 비교"""
    answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2] )
    return answer