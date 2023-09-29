import sys
from collections import deque

n = int(sys.stdin.readline())
num = deque([i for i in range(1, n+1)])

while(len(num) > 1):
    num.popleft()
    num.append(num[0])
    num.popleft()

answer = num[0]
print(answer)