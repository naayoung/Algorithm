import sys
input = sys.stdin.readline

car = [0]*100
answer = 0
a, b, c = map(int, input().split())
for i in range(3):
    arrTime, leftTime = map(int, input().split())
    for j in range(arrTime, leftTime):
        car[j] += 1
for i in car:
    if i == 1:
        answer += a
    elif i == 2:
        answer += b*2
    elif i == 3:
        answer += c*3
print(answer)