import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = []

if a > b:
    b, a = a, b

for i in range(a+1, b):
    answer.append(i)
print(len(answer))
print(*answer)