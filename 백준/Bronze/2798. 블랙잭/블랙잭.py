import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
sum = []
answer = 0

for k in range(n-2):
    for i in range(k+1, n-1):
        for j in range(i+1, n):
            if (card[k] + card[i] + card[j]) <= m:
                sum.append(card[k] + card[i] + card[j])
for i in sum:
    if (m - i) <= (m - answer):
        answer = i
print(answer)