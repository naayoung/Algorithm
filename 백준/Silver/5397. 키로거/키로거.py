import sys
input = sys.stdin.readline

case = int(input().strip())
for _ in range(case):
    L = input().strip()
    left = [] #왼쪽 커서
    right = [] #오른쪽 커서

    for i in L:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    result = "".join(left) + "".join(reversed(right))
    print(result)