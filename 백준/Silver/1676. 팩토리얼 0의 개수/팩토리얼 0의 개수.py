import sys, math
input = sys.stdin.readline

n = int(input().strip())
num = math.factorial(n)
count = 0

for i in str(num):
    if i == '0':
        count += 1
    else:
        count = 0
        
print(count)