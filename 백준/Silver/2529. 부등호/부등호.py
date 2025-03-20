import sys
input = sys.stdin.readline

n = int(input())
t = list(input().split())

#중복 숫자 체크
check = [False]*10
num_list = []
ans = []
depth = 0

def checkcheck(pre, cur, c):
    if t[c] == '>' and pre > cur:
        return True
    elif t[c] == '<' and pre < cur:
        return True
    return False

def dfs(depth):
    #완성
    if depth == n+1:
        temp = ''.join(map(str, num_list))
        ans.append(temp)
        return

    for i in range(10):
        if not check[i]:
            #첫번째 숫자
            if depth == 0:
                check[i] = True
                num_list.append(i)
                dfs(depth+1)

                num_list.pop()
                check[i] = False
            else:
                if checkcheck(num_list[-1], i, depth-1):
                    check[i] = True
                    num_list.append(i)
                    dfs(depth+1)

                    num_list.pop()
                    check[i] = False
dfs(0)
ans.sort()

print(ans[-1])
print(ans[0])