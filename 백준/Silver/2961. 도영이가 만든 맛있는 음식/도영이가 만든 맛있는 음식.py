import sys
input = sys.stdin.readline

def made(idx, shin, zzan, use):
    global answer

    if idx == n:
        if use == 0:
            return
        answer = min(answer, abs(shin - zzan))
        return
    
    made(idx+1, shin*ingre[idx][0], zzan+ingre[idx][1], use+1)
    made(idx+1, shin, zzan, use)

n = int(input().strip())
ingre = [list(map(int, input().split())) for _ in range(n)]
answer = 9999999999

made(0, 1, 0, 0)

print(answer)