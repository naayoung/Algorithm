import sys
input = sys.stdin.readline

n = int(input().strip())
names = set()

for _ in range(n):
    name, confirm = input().split()
    if confirm == 'enter':
        names.add(name)
    elif confirm == 'leave':
        names.remove(name)

# 집합을 리스트로 변환 후 정렬
sorted_names = sorted(names, reverse=True)

for name in sorted_names:
    print(name)