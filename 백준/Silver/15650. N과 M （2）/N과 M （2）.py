import sys
input = sys.stdin.readline

def backtrack(s):
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(s, n+1):
        if i not in answer:
            answer.append(i)
            backtrack(i)
            answer.pop()

n, m = map(int, input().split())
answer = []
backtrack(1)