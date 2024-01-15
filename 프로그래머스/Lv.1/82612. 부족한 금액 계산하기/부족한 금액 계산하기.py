def solution(price, money, count):
    answer = -1
    fee = 0
    for i in range(1, count+1):
        fee += price * i
    if fee > money:
        answer = fee - money
    else:
        answer = 0
    return answer