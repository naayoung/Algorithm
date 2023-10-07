import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
answer = []

for i in word:
    if i.isupper():
        answer.append(i.lower())
    else:
        answer.append(i.upper())
print(''.join(answer))