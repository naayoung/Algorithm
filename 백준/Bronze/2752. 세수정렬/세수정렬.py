import sys

input = sys.stdin.readline

answer = list(map(int, input().split()))

answer.sort()
print(*answer)