import sys
input = sys.stdin.readline

ans = []
for _ in range(3):
    ans.append(int(input().strip()))
ans.sort()
print(ans[1])