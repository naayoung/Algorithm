import sys
input = sys.stdin.readline

n, m = map(int,input().split())
pocketmon = {}

for i in range(1, n+1):
    name = input().strip()
    pocketmon[i] = name
    pocketmon[name] = i

for i in range(m):
    answer = input().strip()
    if answer.isalpha(): #문자열이면
        print(pocketmon[answer])
    elif answer.isdigit(): #숫자이면
        print(pocketmon[int(answer)])
