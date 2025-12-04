import sys
input = sys.stdin.readline

N = int(input().strip())
fruits = list(map(int, input().split()))

cnt = {}
ans = 0
start = 0

for end in range(N):
    if fruits[end] in cnt:
        cnt[fruits[end]] += 1
    else:
        cnt[fruits[end]] = 1

    while len(cnt) > 2:
        cnt[fruits[start]] -= 1
        if cnt[fruits[start]] == 0:
            del cnt[fruits[start]]
        start += 1
    ans = max(ans, end-start + 1)

print(ans)