import sys
input = sys.stdin.readline

L = int(input().strip())
A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
D = int(input().strip())

kor_day = A//C
math_day = B//D

if A % C != 0:
    kor_day += 1
if B % D != 0:
    math_day += 1

if kor_day > math_day:
    print(L-kor_day)
else:
    print(L-math_day)