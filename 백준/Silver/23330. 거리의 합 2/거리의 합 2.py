import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()

ans = 0
total = 0
for i in range(n):
    ans += num[i]*i - total
    total += num[i]
print(ans*2)