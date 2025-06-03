import sys
input = sys.stdin.readline

N = int(input().strip())
t_shirt = list(map(int, input().split()))
T, P = map(int, input().split())

cnt_t = 0
for i in t_shirt:
    if i <= T and i > 0:
        cnt_t += 1
    elif i > T:
        if i%T != 0:
            cnt_t += i//T+1
        else:
            cnt_t += i//T
print(cnt_t)
print(N//P, N%P)