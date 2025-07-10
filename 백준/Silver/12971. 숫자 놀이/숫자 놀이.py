import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
P1, P2, P3, X1, X2, X3 = num


ans = 0
for i in range(1, P1*P2*P3):
    if (i%num[0] == num[3]) and (i%num[1] == num[4]) and (i%num[2] == num[5]):
        ans = i
        break
if ans == 0:
    print(-1)
else:
    print(ans)