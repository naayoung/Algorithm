import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y*100)//x

if z >= 99:
    print(-1)
    exit()

low, high = 1, 10**12
ans = -1

while low <= high:
    mid = (low+high)//2
    newZ = ((y+mid)*100)//(x+mid)

    if newZ > z:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(ans)