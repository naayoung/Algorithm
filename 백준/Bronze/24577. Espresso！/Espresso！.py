import sys
input = sys.stdin.readline

n, s = map(int, input().split())
w = s
count = 0

for _ in range(n):
    order = input().strip()
    oz = 0

    if order[-1] == 'L':
        oz = int(order[0])+1
    else:
        oz = int(order[0])
    
    if w < oz:
        w = s-oz
        count += 1
    else:
        w -= oz
    
print(count)