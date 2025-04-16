import sys
input = sys.stdin.readline

R, C = map(int, input().split())
A, B = map(int, input().split())

for r in range(R):
    for a in range(A):
        line = ''
        for c in range(C):
            if (r + c) % 2 == 0:
                line += 'X' * B
            else:
                line += '.' * B
        print(line)