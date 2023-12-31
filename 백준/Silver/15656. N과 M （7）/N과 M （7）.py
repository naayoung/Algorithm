import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
answer = []

def back():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in num:
        answer.append(i)
        back()
        answer.pop()

back()