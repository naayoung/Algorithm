import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
num = deque(enumerate(map(int, input().split())))
answer = []

while num:
    idx, paper = num.popleft()
    answer.append(idx + 1)

    if paper > 0:
        num.rotate(-(paper - 1))
    elif paper < 0:
        num.rotate(-paper)
print(*answer)