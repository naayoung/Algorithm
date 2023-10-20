import sys, collections
input = sys.stdin.readline

n = int(input())
x = collections.deque([])

for i in range(n):
    comm = input().split()
    if comm[0] == "push":
       x.append(comm[1])
    elif comm[0] == "pop":
        if len(x) == 0:
            print(-1)
        else:
            print(x.popleft())
    elif comm[0] == "size":
        print(len(x))
    elif comm[0] == "empty":
        if len(x) == 0:
            print(1)
        else:
            print(0)
    elif comm[0] == "front":
        if len(x) == 0:
            print(-1)
        else:
            print(x[0])
    elif comm[0] == "back":
        if len(x) == 0:
            print(-1)
        else:
            print(x[-1])