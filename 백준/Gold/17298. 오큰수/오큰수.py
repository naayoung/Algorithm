import sys
input = sys.stdin.readline

N = int(input().strip())
num = list(map(int, input().split()))

stack = []
answer = [-1] * N
for i in range(N):
    while stack and num[stack[-1]] < num[i]:
        answer[stack.pop()] = num[i]
    stack.append(i)
print(*answer)