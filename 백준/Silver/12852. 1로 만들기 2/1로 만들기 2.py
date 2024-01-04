import sys
input = sys.stdin.readline

n = int(input().strip())
d = [0] * (n+1)
answer = ["" for _ in range(n+1)]
answer[1] = "1"

for i in range(2, n+1):
    d[i] = d[i-1]+1
    prev = i-1

    if i%3 == 0 and d[i//3]+1 < d[i]:
        d[i] = d[i//3]+1
        prev = i//3
    if i%2 == 0 and d[i//2]+1 < d[i]:
        d[i] = d[i//2]+1
        prev = i//2
    answer[i] = str(i) + " " + answer[prev]
print(d[n])
print(answer[n])