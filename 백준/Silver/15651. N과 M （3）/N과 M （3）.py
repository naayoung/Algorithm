import sys
input = sys.stdin.readline

def back():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        back()
        answer.pop()

n, m = map(int, input().split())
answer = []
back()