import sys
input = sys.stdin.readline

N, M = map(int, input().split())
confirm = []
for n in range(N):
    name, s = input().split()
    s = int(s)

    confirm.append((name, s))

for m in range(M):
    temp = int(input().strip())
    start, end = 0, N-1
    ans = 0

    while start <= end:
        mid = (start+end)//2

        if temp <= confirm[mid][1]:
            ans = mid
            end = mid-1
        else:
            start = mid+1

    print(confirm[ans][0])