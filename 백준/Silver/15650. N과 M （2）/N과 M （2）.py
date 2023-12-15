import sys
input = sys.stdin.readline

def back(start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            back(i)
            answer.pop()

n, m = map(int, input().split())
answer = []

back(1)