import sys
from math import gcd
input = sys.stdin.readline

def lcm(a, b):
    if a*b == n:
        return True
    return False

def check(a, b):
    if gcd(a, b) == 1:
        if lcm(a, b):
            return True
    return False

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    temp = int(n**0.5)
    ans = 0
    if n == 1:
        ans = 1
    else:
        for i in range(1, temp+1):
            if n%i == 0:
                a, b = i, n//i
                if b > a:
                    if check(a, b):
                        ans += 1
    print(ans)