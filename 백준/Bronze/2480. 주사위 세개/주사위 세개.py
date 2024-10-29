import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
cnt = {}
answer = 0

for i in num:
    cnt[i] = num.count(i)
cnt = dict(sorted(cnt.items(), key=lambda x:-x[1]))

if max(cnt.values()) == 3:
    answer = 10000+num[0]*1000
if max(cnt.values()) == 2:
    answer = 1000+list(cnt)[0]*100
if max(cnt.values()) == 1:
    answer = max(num)*100
print(answer)