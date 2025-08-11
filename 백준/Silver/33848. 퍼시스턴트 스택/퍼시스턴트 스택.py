import sys
input = sys.stdin.readline

q = int(input().strip())
s = []
temp = []
for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        temp.append((1, query[1]))
        s.append(query[1])
    elif query[0] == 2:
        temp.append((2, s[-1]))
        s.pop()
    elif query[0] == 3:
        for i in range(query[1]):
            if temp:
                last_op, last_value = temp.pop()
                if last_op == 1:
                    s.remove(last_value)
                elif last_op == 2:
                    s.append(last_value)
            else:
                break
    elif query[0] == 4:
        print(len(s))
    elif query[0] == 5:    
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])