def solution(n, computers):
    visited = [0] * n
    count = 0
    
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count