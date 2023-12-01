import sys
from collections import deque
input = sys.stdin.readline

answer = []
num = int(input().strip())
card = [_ for _ in range(1, num+1)]
cards = deque(card)

for _ in range(num):
    answer.append(cards.popleft())
    cards.rotate(-1)
print(*answer)