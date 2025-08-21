import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    ans = ""
    big = 0
    for _ in range(n):
        s, l = input().split()
        l = int(l)

        if big < l:
            ans = s
            big = l
    print(ans)
