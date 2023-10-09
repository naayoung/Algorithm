import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    apartment = [i for i in range(1, n+1)]
    answer = 0

    for i in range(k-1):
        for j in range(1, n):
            apartment[j] = apartment[j] + apartment[j-1]

    for i in range(n):
        answer += apartment[i]
    print(answer)