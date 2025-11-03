import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input().strip())
PandQ = defaultdict(list)

for _ in range(N):
    a, _, b = input().split()
    PandQ[a].append(b)

visited = set(['Baba'])
res = set()

dq = deque()

if 'Baba' in PandQ:
    for next in PandQ['Baba']:
        if next not in visited:
            visited.add(next)
            dq.append(next)
            res.add(next)

while dq:
    u = dq.popleft()

    if u in PandQ:
        for v in PandQ[u]:
            if v not in visited:
                visited.add(v)
                dq.append(v)
                res.add(v)

for name in sorted(res):
    print(name)