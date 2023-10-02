import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hear = set([str(input()) for _ in range(n)])
see = set([str(input()) for _ in range(m)])

result = sorted(hear&see)

print(len(result))
for i in result:
    print(i.strip())