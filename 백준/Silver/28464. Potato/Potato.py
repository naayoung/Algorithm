import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
potato = list(map(int, input().split()))
potato.sort()
potato = deque(potato)

s, p = 0, 0

for i in range(n):
    if(i%2 != 0):
        s += potato.popleft()
    else:
        p += potato.pop()

print(s, p)