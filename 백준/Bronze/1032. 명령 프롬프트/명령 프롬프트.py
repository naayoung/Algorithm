import sys
input = sys.stdin.readline

n = int(input().strip())
dir = []
for _ in range(n):
    dir.append(input().strip())
temp = dir[0]
ans = []
for d in dir:
    for i in range(len(d)):
        if d[i] == temp[i]:
            ans.append(d[i])
        else:
            ans.append('?')
    temp = ''.join(ans)
    ans = []
print(temp)