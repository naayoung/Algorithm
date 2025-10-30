import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())
dom = [input().strip() for _ in range(n)]
kat = [input().strip() for _ in range(n)]

cnt = sum((Counter(dom) & Counter(kat)).values())
print(cnt)