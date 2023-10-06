import sys
input = sys.stdin.readline

n = int(input())
x = []
answer = []

for i in range(n):
    comm = list(map(str, input().split()))

    if comm[0] == "push":
        x.append(comm[1])
    elif comm[0] == "pop":
        if len(x) == 0:
            answer.append(-1)
        else:
            answer.append(x[len(x)-1])
            del x[len(x)-1]
    elif comm[0] == "size":
        answer.append(len(x))
    elif comm[0] == "empty":
        if len(x) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif comm[0] == "top":
        if len(x) == 0:
            answer.append(-1)
        else:
            answer.append(x[len(x)-1])
for i in answer:
    print(i)