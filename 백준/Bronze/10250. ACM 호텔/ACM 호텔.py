import sys
input = sys.stdin.readline

t = int(input())
answer = 0

for i in range(t):
    h, w, n = list(map(int, input().split()))
    count = 0
    while True:
        count += 1
        if n > h:
            n = n - h
        elif n <= h:
            answer = n*100+count
            print(answer)
            break