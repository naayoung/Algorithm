import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = 1
con = []

for _ in range(n):
    d, c = map(int, input().split())
    con.append([d, c])
con.sort()
price = con[0][1]

for i in range(1, n):
    if con[i][1] < price:
        cnt += 1
        price = con[i][1]

print(cnt)