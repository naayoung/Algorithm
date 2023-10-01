import sys
input = sys.stdin.readline

m, n = list(map(int,input().split()))
num = [True] * (n+1)
nn = int(n**0.5)

for i in range(2, nn+1):
    if(num[i]):
        for j in range(i+i, n+1, i):
            num[j] = False
for i in range(m, n+1):
    if(i == 1):
        num[i] = False
    elif(num[i]):
        print(i)