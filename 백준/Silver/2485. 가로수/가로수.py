import sys
import math
input = sys.stdin.readline

N = int(input().strip())
tree = []
before = 0
for n in range(N):
    temp = int(input().strip())
    if n == 0:
        before = temp
    else:
        tree.append(temp-before)
        before = temp

tree_gcd = math.gcd(tree[0], tree[1])
for t in range(2, N-1):
    tree_gcd = math.gcd(tree_gcd, tree[t])

ans = 0
for i in tree:
    ans += i//tree_gcd-1

print(ans)