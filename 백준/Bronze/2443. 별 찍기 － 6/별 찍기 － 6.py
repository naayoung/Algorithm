import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0
for i in range(n, 0, -1):
    print(count*" "+(2*i-1)*"*")
    count += 1