import sys, math
input = sys.stdin.readline

a, b = map(int,input().split())
a1, b1 = map(int,input().split())

an1 = a*b1 + a1*b
an2 = b*b1

print(an1//math.gcd(an1, an2), an2//math.gcd(an1, an2))