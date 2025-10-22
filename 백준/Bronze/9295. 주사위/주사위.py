import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    a, b = map(int, input().split())
    ans = 'Case '+str(t+1)+':'
    print(ans, a+b)