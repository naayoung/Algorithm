import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
answer = '1'*gcd(a, b)
print(answer)
    