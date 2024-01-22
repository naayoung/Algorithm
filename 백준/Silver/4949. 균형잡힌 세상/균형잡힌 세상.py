import sys
input = sys.stdin.readline

while True:
    sentence = str(input().rstrip())
    temp = []

    if sentence == ".":
        break
    
    for i in sentence:
        if i == "[" or i == "(":
            temp.append(i)
        elif i == "]":
            if len(temp) != 0 and temp[-1] == "[":
                temp.pop()
            else:
                temp.append(i)
                break
        elif i == ")":
            if len(temp) != 0 and temp[-1] == "(":
                temp.pop()
            else:
                temp.append(i)
                break
    if len(temp) == 0:
        print("yes")
    else:
        print("no")