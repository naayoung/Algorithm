import sys
input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    num = input().strip().split()
    if(num[0] == "all" or num[0] == "empty"):
        if(num[0] == "all"):
            s = set([j for j in range(1, 21)])
        else:
            s.clear()
    else:
        if(num[0] == "add"):
            if int(num[1]) not in s:
                s.add(int(num[1]))
        elif(num[0] == "check"):
            if int(num[1]) in s:
                print(1)
            else:
                print(0)
        elif(num[0] == "remove"):
            if int(num[1]) in s:
                s.remove(int(num[1]))
        elif(num[0] == "toggle"):
            if int(num[1]) in s:
                s.remove(int(num[1]))
            else:
                s.add(int(num[1]))