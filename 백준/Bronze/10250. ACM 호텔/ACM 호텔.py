import sys
input = sys.stdin.readline

t = int(input())
answer = 0

for i in range(t):
    h, w, n = list(map(int, input().split()))
    count = 0
    while True:
        if n > h:
            count += 1
            n = n - h
        elif n <= h:
            count += 1
            answer = n*100+count
            print(answer)
            break