import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

abc = a*b*c
answer = {i : 0 for i in range(10)}

for i in str(abc):
    i = int(i)
    if i == 0:
        answer[i] += 1
    elif i == 1:
        answer[i] += 1
    elif i == 2:
        answer[i] += 1
    elif i == 3:
        answer[i] += 1
    elif i == 4:
        answer[i] += 1
    elif i == 5:
        answer[i] += 1
    elif i == 6:
        answer[i] += 1
    elif i == 7:
        answer[i] += 1
    elif i == 8:
        answer[i] += 1
    elif i == 9:
        answer[i] += 1

for i in answer.values():
    print(i)