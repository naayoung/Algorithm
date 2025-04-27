from sys import stdin
input=stdin.readline

def dfs(x,y,v):
    global ans,ans2
    if x==y==n-1:
        ans=max(ans,eval(v))
        ans2=min(ans2,eval(v))
        return
    try:
        dfs(x+1,y,v+arr[x+1][y] if (x+y)%2==0 else str(eval(v+arr[x+1][y])))
    except:
        pass
    try:
        dfs(x,y+1,v+arr[x][y+1]if (x+y)%2==0 else str(eval(v+arr[x][y+1])))
    except:
        pass



n=int(input())
ans=-10**10
ans2=10**10

arr=[list(input().rstrip().split()) for i in range(n)]

dfs(0,0,arr[0][0])
print(ans,ans2)