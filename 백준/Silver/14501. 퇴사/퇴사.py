import sys
input = sys.stdin.readline

def meet(idx, price):
    global answer

    if idx == n:
        answer = max(answer, price)
        return
    if idx > n-1:
        return

    meet(idx+plan[idx][0], price+plan[idx][1])
    meet(idx+1, price)

n = int(input().strip())
plan = [list(map(int, input().split())) for _ in range(n)]
answer = 0

meet(0, 0)

print(answer)