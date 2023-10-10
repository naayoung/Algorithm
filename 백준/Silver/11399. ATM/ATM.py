import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()
answer = 0

for i in range(1, n+1):
    time = sum(p[0:i])
    answer += time
print(answer)