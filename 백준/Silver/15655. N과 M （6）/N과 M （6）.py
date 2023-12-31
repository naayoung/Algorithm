import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
answer = []

def back(start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(start, n):
        if num[i] not in answer:
            answer.append(num[i])
            back(i+1)
            answer.pop()

back(0)
