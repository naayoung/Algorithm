import sys

input = sys.stdin.readline
answer = []

for _ in range(7):
    temp = int(input().strip())
    if temp%2 != 0:
        answer.append(temp)

if len(answer) > 0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)