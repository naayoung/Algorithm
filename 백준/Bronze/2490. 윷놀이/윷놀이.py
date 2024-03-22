import sys

input = sys.stdin.readline

for i in range(3):
    num = list(map(int, input().split()))
    count = 0
    
    for i in num:
        if i == 0:
            count += 1
    if count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
    elif count == 0:
        print("E")