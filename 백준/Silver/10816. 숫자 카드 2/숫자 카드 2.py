import sys
input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))
ns_count = {}
answer = []

for i in ns:
    if i not in ns_count:
        ns_count[i] = 1
    else:
        ns_count[i] += 1

for i in ms:
    if i in ns_count:
        answer.append(ns_count[i])
    else:
        answer.append(0)
print(*answer)