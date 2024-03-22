import sys

input = sys.stdin.readline
card = [_ for _ in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    a -= 1

    card[a:b] = card[a:b][::-1]
print(*card)