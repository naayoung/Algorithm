import sys
input = sys.stdin.readline

n = int(input().strip())
f, answer = 1, 1

for i in range(1, n+1):
    f *= i
answer = f // (7*24*60*60)
print(answer)