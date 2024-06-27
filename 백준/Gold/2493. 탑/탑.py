import sys
input = sys.stdin.readline

N = int(input().strip())
top = list(map(int, input().split()))

stack = [] #탑 인덱스와 높이 저장
answer = [0] * N
for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, top[i]))
print(*answer)