import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
temp = []
target = 1

for i in num:
    temp.append(i)
    while temp and temp[-1] == target:
        temp.pop()
        target += 1
    if len(temp) > 1 and temp[-1] > temp[-2]:
        print("Sad")
        sys.exit()
if temp:
    print("Sad")
else:
    print("Nice")