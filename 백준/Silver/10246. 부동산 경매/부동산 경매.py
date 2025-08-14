import sys
memo = [0] * 10000001
for i in range(1, 10000000):
    temp = 0
    j = i
    while temp <= 10000000:
        temp += j + 1
        j += 1
        if temp > 10000000:
            break
        memo[temp] += 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        sys.exit()
    print(memo[N])