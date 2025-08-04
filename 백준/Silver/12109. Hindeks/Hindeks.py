import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort(reverse=True)

for i in range(n):
    if num[i] < i + 1:
        print(i)
        break
else:
    print(n)