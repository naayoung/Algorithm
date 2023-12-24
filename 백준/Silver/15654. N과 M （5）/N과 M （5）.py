import sys
input = sys.stdin.readline

def back():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in num:
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
answer = []
back()