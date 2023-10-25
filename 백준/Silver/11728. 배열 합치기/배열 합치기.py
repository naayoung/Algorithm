import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
answer = num1 + num2
answer.sort()
print(*answer)