import sys
input = sys.stdin.readline

A, B = input().split()

sum_A = sum(map(int, A))
sum_B = sum(map(int, B))

print(sum_A * sum_B)