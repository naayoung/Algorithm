import sys
input = sys.stdin.readline

S = input()
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

answer = [0 for _ in range(26)]
for i in S:
    if i in alpabet:
        temp = alpabet.index(i)
        answer[temp] = answer[temp] + 1
print(*answer)