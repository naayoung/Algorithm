import sys
input = sys.stdin.readline

N = int(input().strip())
building = []
for _ in range(N):
    building.append(int(input().strip()))

stack = []
count = 0
for i in range(N):
    while stack and stack[-1] <= building[i]:
        stack.pop()
    stack.append(building[i])
    count += len(stack) - 1
print(count)