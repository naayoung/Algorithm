import sys
input = sys.stdin.readline

L, R = input().split()
answer = 0

if len(L) != len(R):
    answer = 0
else:
    for i in range(len(L)):
        if L[i] != R[i]:
            break
        else:
            if L[i] == '8':
                answer += 1
print(answer)