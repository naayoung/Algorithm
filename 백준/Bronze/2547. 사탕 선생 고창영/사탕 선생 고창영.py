import sys
input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    temp = input()
    n = int(input().strip())
    candy = []

    for j in range(n):
        candy.append(int(input().strip()))
    if sum(candy)%n == 0:
        print("YES")
    else:
        print("NO")