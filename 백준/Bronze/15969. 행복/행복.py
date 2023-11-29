import sys
input = sys.stdin.readline

N = int(input().strip())
score = list(map(int, input().split()))

max_score = max(score)
min_score = min(score)

print(max_score - min_score)