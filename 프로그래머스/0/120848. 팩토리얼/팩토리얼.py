import math

def solution(n):
    answer = 0
    temp = 0
    for i in range(11):
        if math.factorial(i) <= n:
            answer = i
    return answer