import sys
input = sys.stdin.readline

N = int(input().strip())
first, last = input().strip().split("*")

for _ in range(N):
    temp = input().strip()

    if len(temp) < len(first) + len(last):
        print("NE")
    elif temp[:len(first)] == first and temp[-len(last):] == last:
        print("DA")
    else:
        print("NE")