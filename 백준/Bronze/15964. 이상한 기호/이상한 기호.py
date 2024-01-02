import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = (a+b)*(a-b)
print(answer)