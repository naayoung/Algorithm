def solution(box, n):
    answer = 1
    num = []
    for i in box:
        num.append(i//n)
    for i in num:
        answer *= i
    return answer