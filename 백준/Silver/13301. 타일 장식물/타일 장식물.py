import sys
input = sys.stdin.readline

n = int(input().strip())
ans = [1, 2]
for i in range(1, n-1):
    temp = ans[i-1] + ans[i]
    ans.append(temp)
print(sum(ans[n-2:])*2)