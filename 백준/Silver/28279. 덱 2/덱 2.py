import sys,collections
input = sys.stdin.readline

n = int(input())
x = collections.deque([])
for i in range(n):
    num = input().split()

    if num[0] == '1':
        x.appendleft(num[1])
    elif num[0] == '2':
        x.append(num[1])
    elif num[0] == '3':
        if len(x) == 0:
            print(-1)
        else:
            print(x.popleft())
    elif num[0] == '4':
        if len(x) == 0:
            print(-1)
        else:
            print(x.pop())
    elif num[0] == '5':
        print(len(x))
    elif num[0] == '6':
        if len(x) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == '7':
        if len(x) == 0:
            print(-1)
        else:
            x.appendleft(x[0])
            print(x.popleft())
    elif num[0] == '8':
        if len(x) == 0:
            print(-1)
        else:
            x.append(x[-1])
            print(x.pop())