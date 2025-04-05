import sys
input = sys.stdin.readline

N = int(input().strip())
pre, pos = input().strip().split("*")

ans = []
for _ in range(N):
    temp = input().strip()

    # 길이 자체가 짧으면 무조건 실패
    if len(temp) < len(pre) + len(pos):
        ans.append("NE")
        continue

    if temp.startswith(pre) and temp.endswith(pos):
        ans.append("DA")
    else:
        ans.append("NE")

for a in ans:
    print(a)
