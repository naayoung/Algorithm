import sys
input = sys.stdin.readline

t = int(input())
tc = [list(map(int, input().split(','))) for _ in range(t)]

for i in tc:
    print(sum(i))