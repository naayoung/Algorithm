import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    ans = 0
    power = 1  # 3^0부터 시작
    while N > 0:
        if N & 1:
            ans += power
        power *= 3
        N >>= 1
    print(ans)