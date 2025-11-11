import sys
input = sys.stdin.readline

p = [12, 11, 11, 10, 9, 9, 9, 8, 7, 6, 6]
m = [1600, 894, 1327, 1311, 1004, 1178, 1357, 837, 1055, 556, 773]

n = int(input().strip())
print(p[n-1], m[n-1])