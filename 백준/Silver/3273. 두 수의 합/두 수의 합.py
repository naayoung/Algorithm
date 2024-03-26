import sys
input = sys.stdin.readline

n = int(input().strip())
num = list(map(int, input().split()))
x = int(input().strip())

count = 0
start, end = 0, n-1

num.sort()

while start < end:
    Sum = num[start] + num[end]
    
    if Sum > x:
        end -= 1
    elif Sum < x:
        start += 1
    else:
        count += 1
        end -= 1
        start += 1
print(count)