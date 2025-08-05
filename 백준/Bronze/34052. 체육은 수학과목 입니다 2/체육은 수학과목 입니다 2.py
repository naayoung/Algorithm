import sys
input = sys.stdin.readline

time = 0
for _ in range(4):
    i = int(input().strip())
    time += i

if time+300 <= 1800:
    print("Yes")
else:
    print("No")