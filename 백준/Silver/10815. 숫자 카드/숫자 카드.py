import sys
input = sys.stdin.readline

n = int(input())
num = set(input().split())
m = int(input())
num2 = input().split()
answer = []

for i in num2:
    if i in num:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)