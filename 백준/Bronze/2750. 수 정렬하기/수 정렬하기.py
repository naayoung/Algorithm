import sys
input = sys.stdin.readline

n = int(input())
num = [int(input().strip()) for _ in range(n)]
answer = []

for i in num:
    if i not in answer:
        answer.append(i)
answer.sort()

for i in answer:
    print(i)