import sys
input = sys.stdin.readline

N = int(input().strip())
H = list(map(int, input().split()))
MOD = 10**9 + 7

H.sort(reverse=True)

total = 0
for h in H:
    total = (total * 2 + h) % MOD
print(total % MOD)