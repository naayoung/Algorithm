import sys
input =  sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    number = list(map(str, input().split()))
    num.append(number)

num.sort(key = lambda x : (int(x[1]), int(x[0])))

for i in num:
    print(' '.join(i))