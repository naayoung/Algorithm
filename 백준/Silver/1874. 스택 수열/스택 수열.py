import sys
input = sys.stdin.readline

n = int(input())
num = [int(input().strip()) for _ in range(n)]
test = [i for i in range(n+1)]
answer = []

count = 0

while True:
    if count >= len(test):
        print("NO")
        break
    elif num[0] <= test[count]:
        answer.append("-")
        del num[0]
        del test[count]
        count -= 1
        if len(num) == 0:
            for i in answer:
                print(i)
            break
    else:
        answer.append("+")
        count += 1
