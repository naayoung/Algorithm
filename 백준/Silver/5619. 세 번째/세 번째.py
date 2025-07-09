import sys
input = sys.stdin.readline

num = []
n = int(input().strip())
for _ in range(n):
    num.append(int(input().strip()))

num.sort()
limit = min(10, n)

ans = []
for i in range(limit):
    for j in range(limit):
        if i != j:
            ans.append(int(str(num[i]) + str(num[j])))

ans.sort()
print(ans[2]) 