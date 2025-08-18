import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    word, i, j = input().split()
    i, j = int(i), int(j)

    ans = ''
    ans = word[:i] + word[j:]
    print(ans)