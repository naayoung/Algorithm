import sys
input = sys.stdin.readline

def backtrack():
    if len(ans) == n:
        print(*ans)
        return
    
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            backtrack()
            ans.pop()

n = int(input().strip())
ans = []

backtrack()