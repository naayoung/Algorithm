import sys
input = sys.stdin.readline

def backtrack(depth, we, visited):  
    global cnt

    if we < 500:
        return
    if depth == n:
        cnt += 1
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth+1, we-k+weight[i], visited)
            visited[i] = False

n, k = map(int, input().split())
weight = list(map(int, input().split()))

cnt = 0
visited = [False]*n
backtrack(0, 500, visited)
print(cnt)
