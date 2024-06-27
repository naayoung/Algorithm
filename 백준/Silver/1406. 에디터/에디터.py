import sys
input = sys.stdin.readline

word = list(input().strip())
M = int(input().strip())

temp = []
for _ in range(M):
    command = list(input().split())
    if command[0] == "L":
        if word:
            temp.append(word.pop())
    elif command[0] == "D":
        if temp:
            word.append(temp.pop())
    elif command[0] == "B":
        if word:
            word.pop()
    elif command[0] == "P":
        word.append(command[1])
result = "".join(word) + "".join(reversed(temp))
print(result)