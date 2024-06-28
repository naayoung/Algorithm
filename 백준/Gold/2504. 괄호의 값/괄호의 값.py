import sys
input = sys.stdin.readline

t = input().strip()

stack = []

temp = 1
answer = 0
for i in range(len(t)):
    if t[i] == "(":
        stack.append("(")
        temp *= 2
    elif t[i] == "[":
        stack.append("[")
        temp *= 3
    elif t[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if t[i-1] == "(":
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer=0
            break
        if t[i-1] =='[':
            answer+=temp
        stack.pop()
        temp //= 3
if stack:
    print(0)
else:
    print(answer)