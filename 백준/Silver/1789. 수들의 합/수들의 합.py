import sys

input = sys.stdin.readline

s = int(input().strip())
count = 0
total = 0

while True:
    count += 1
    total += count

    if total > s:
        break

print(count-1)
