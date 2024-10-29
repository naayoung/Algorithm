import sys
input = sys.stdin.readline

n = input().strip()
cnt = 0

if int(n) < 10:
    n = '0'+ n

t = n
while int(n) != int(t) or cnt == 0:
    temp = str(int(t[0]) + int(t[1]))
    t = t[1] + temp[len(temp)-1]
    cnt += 1
print(cnt)