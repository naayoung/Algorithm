import sys
input = sys.stdin.readline

r = int(input().strip())
g = int(input().strip())
b = int(input().strip())

c = r*3 + g*4 + b*5

print(c)