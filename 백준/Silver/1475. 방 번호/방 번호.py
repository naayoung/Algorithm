import sys
input = sys.stdin.readline

S = str(input().strip())
answer = [0 for _ in range(10)]

for i in S:
    if i == '6' or i == '9':
        if answer[6] == answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    else:
        answer[int(i)] += 1
print(max(answer))
