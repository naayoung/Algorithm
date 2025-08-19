import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    s = input().strip()

    cnt = 0
    for _ in s:
        cnt += 1
    
    if cnt >= 6 and cnt <= 9:
        print("yes")
    else:
        print("no")