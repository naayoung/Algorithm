import sys
input = sys.stdin.readline

S = input().rstrip()
answer = []

for i in range(len(S)):
    answer.append(S[i:len(S)])
answer.sort()

for i in answer:
    print(i)