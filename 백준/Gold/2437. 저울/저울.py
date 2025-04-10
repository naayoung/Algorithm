N = int(input())
weights = list(map(int, input().split()))
weights.sort()

target = 1  # 측정 가능한 최소 무게

for w in weights:
    if w > target:
        break
    target += w

print(target)