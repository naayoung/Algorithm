import sys
import math
input = sys.stdin.readline

# 소수 판별
def primenumber(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


while True:
    num = int(input().strip())
    if num == 0:
        break

    answer = 0
    for i in range(2, num//2 + 1):
        if primenumber(i) and primenumber(num-i):
            answer += 1
    print(answer)
