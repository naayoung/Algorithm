import sys
input = sys.stdin.readline

n = input().strip()
ans = 0

for i in n:
    i = int(i)**5
    ans += i
print(ans)