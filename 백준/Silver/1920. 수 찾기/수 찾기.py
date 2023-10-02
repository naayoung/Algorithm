import sys
input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))
count = {}

for i in ns:
    count[i] = 1

for i in ms:
    if i in count:
        print(count[i])
    else:
        print(0)