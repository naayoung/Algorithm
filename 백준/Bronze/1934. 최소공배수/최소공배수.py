import sys, math
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))
    answer = math.lcm(a, b)
    print(answer) 