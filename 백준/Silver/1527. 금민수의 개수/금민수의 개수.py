import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def count(x, a, b):
    cnt = 0
    if x > b:
        return 0

    if a <= x <= b:
        cnt += 1
    
    cnt += count(x*10 + 4, a, b)
    cnt += count(x*10 + 7, a, b)

    return cnt

cnt = count(0, a, b)
print(cnt)