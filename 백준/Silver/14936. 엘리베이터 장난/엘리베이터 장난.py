n, m = map(int, input().split())
case1 = n
case2 = n//2
case3 = (n+1)//2
case4 = (n-1)//3+1

cnt = 1
#동작1
if case1 <= m:
    cnt += 1
#동작2
if case2 <= m and n > 1:
    cnt += 1
#동작3
if case3 <= m and n > 1:
    cnt += 1
#동작4
if case4 <= m and n > 2:
    cnt += 1
#동작1+동작4
if case1+case4 <= m and n >= 3:
    cnt += 1
#동작2+동작4
if case2+case4 <= m and n >= 3:
    cnt += 1
#동작3+동작4
if case3+case4 <= m and n >= 3:
    cnt += 1

print(cnt)