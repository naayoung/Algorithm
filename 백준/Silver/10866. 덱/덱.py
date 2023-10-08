import sys
input = sys.stdin.readline

n = int(input())
x = []
deq = []
answer = []

for i in range(n):
    x = list(map(str, input().split()))
    if x[0] == "push_front":
        deq.insert(0, x[1])
    elif x[0] == "push_back":
        deq.append(x[1])
    elif x[0] == "pop_front":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq[0])
            del deq[0]
    elif x[0] == "pop_back":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq[-1])
            del deq[-1]
    elif x[0] == "size":
        answer.append(len(deq))
    elif x[0] == "empty":
        if len(deq) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif x[0] == "front":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq[0])
    elif x[0] == "back":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq[-1])
for i in answer:
    print(i)