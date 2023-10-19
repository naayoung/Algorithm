import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
answer = {}

for i in num:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1
answer = dict(sorted(answer.items()))
print(max(answer, key=answer.get))