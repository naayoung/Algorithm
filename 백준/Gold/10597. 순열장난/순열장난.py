import sys
input = sys.stdin.readline

kriii = input().strip()
L = len(kriii)

# N 계산: 길이 9 이하면 N=L, 아니면 (L+9)//2
if L <= 9:
    N = L
else:
    N = (L + 9) // 2

visited = [False]*(N+1)
visited[0] = True

ans = []

def check(index):
    if index == len(kriii):
        print(*ans)
        return True

    # 1개인경우
    if kriii[index] != '0':
        temp = int(kriii[index])
        if visited[temp] != True:
            ans.append(temp)
            visited[temp] = True

            if check(index+1):
                return True
            ans.pop()
            visited[temp] = False

    # 2개인경우
    if index+1 < len(kriii):
        temp = int(kriii[index]+kriii[index+1])
        if 10 <= temp <= N and visited[temp] != True:
            ans.append(temp)
            visited[temp] = True

            if check(index+2):
                return True
            ans.pop()
            visited[temp] = False

    return False

check(0)