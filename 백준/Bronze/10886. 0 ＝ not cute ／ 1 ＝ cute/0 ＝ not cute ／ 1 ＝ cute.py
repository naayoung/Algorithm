import sys
input = sys.stdin.readline

n = int(input().strip())
cute, notcute = 0, 0
for i in range(n):
    t = int(input().strip())
    if t == 1:
        cute += 1
    else:
        notcute += 1

if cute > notcute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")