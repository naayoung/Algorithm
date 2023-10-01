import sys
input = sys.stdin.readline

t = int(input())
test = [str(input()).strip() for _ in range(t)]

for i in test:
    for _ in range(len(i)):
        if "()" in i:
            i = i.replace("()", "")
    if(len(i) == 0):
        print("YES")
    else:
        print("NO")