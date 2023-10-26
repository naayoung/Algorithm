import sys
input = sys.stdin.readline

num = [list(map(int,input().split())) for _ in range(9)]
answer = []
answer2 = []

for i in num:
    answer.append(max(i))
    answer2.append(i.index(max(i)))
print(max(answer))

a = answer.index(max(answer))
b = answer2[a]
print(a+1, b+1)
