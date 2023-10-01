import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
count = 0
answer = 0

for i in num:
    for j in range(1, i+1):
        if(i == 1):
            break
        elif(i%j == 0):
            count += 1
    if(count == 2):
        answer += 1
        count = 0
    else:
        count = 0
print(answer)