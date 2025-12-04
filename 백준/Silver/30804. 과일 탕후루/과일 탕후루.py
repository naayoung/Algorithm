import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
fruits = list(map(int, input().split()))

cnt = defaultdict(int)
left = 0
ans = 0

for right in range(N):
    cnt[fruits[right]] += 1

    while len(cnt) > 2:
        cnt[fruits[left]] -= 1
        if cnt[fruits[left]] == 0:
            del cnt[fruits[left]]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)