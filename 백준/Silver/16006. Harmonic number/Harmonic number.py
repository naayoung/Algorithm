import math

N = int(input())

P, Q = 0, 1
for i in range(1, N+1):
    Q *= i
for i in range(1, N+1):
    P += Q//i

temp = math.gcd(P, Q)
p, q = P//temp, Q//temp

print(p)
print(q)
