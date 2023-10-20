import sys, collections
input = sys.stdin.readline

n = int(input())
x = collections.deque([])

for i in range(n):
    num = input().split()

    if num[0] == '1':
        x.append(num[1])
    elif num[0] == '2':
        if len(x) == 0:
            print(-1)
        else:
            print(x.pop())
    elif num[0] == '3':
        print(len(x))
    elif num[0] == '4':
        if len(x) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == '5':
        if len(x) == 0:
            print(-1)
        else:
            x.append(x[-1])
            print(x.pop())