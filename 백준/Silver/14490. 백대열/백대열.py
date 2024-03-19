import sys, math

input = sys.stdin.readline

n, m = map(int, input().split(":"))
temp = math.gcd(n, m)

print('%d:%d' %(n//temp, m//temp))