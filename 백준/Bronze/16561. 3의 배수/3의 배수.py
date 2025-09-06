import sys
input = sys.stdin.readline

n = int(input().strip())

ans = 0
new_n = n//3
ans = (new_n-1)*(new_n-2)//2
print(ans)