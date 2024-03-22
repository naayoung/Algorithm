import sys

input = sys.stdin.readline

N = int(input())
free = list(map(int, input().split()))

Y, M = 0, 0

for i in free:
    if i >= 30:
        Y += 10 * (i//30)
        if i%30 >= 0:
            Y += 10
    else:
        Y += 10

    if i >= 60:
        M += 15 * (i//60)
        if i%60 >= 0:
            M += 15
    else:
        M += 15
if Y == M:
    print("Y M", Y)
elif Y < M:
    print("Y", Y)
elif M < Y:
    print("M", M)