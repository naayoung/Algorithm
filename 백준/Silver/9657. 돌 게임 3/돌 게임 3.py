import sys
input = sys.stdin.readline

N = int(input().strip())
ans = ''
if N % 7 == 0 or N % 7 == 2:
    ans = 'CY'
else:
    ans = 'SK'
print(ans)