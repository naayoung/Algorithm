import sys, collections
input = sys.stdin.readline

n, k = map(int, input().split())
num = collections.deque([i for i in range(1, n+1)])
answer = []

while True:
    if len(num) != 0:
        num.rotate(-k+1)
        answer.append(num.popleft())
    else:
        break

print("<", end="")
for i in range(n):
    if i < n-1:
        print(answer[i], end = ", ")
    else:
        print(answer[i], end = "")
print(">")
