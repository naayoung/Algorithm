import sys
input = sys.stdin.readline

n, m = map(int, input().split())
brand = list(map(int, input().split()))
count = []

for i in range(1, m+1):
    count.append(brand.count(i))

print(max(count))