import sys
input = sys.stdin.readline

t = input().strip()

stack = []
count = 0
for i in range(len(t)):
    if t[i] == "(":
        stack.append("(")
    else:
        if t[i-1] == "(":
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)