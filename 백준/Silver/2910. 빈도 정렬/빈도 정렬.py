import sys

input = sys.stdin.readline

n, c = map(int, input().split())
num = list(map(int, input().split()))

dic = {}
answer = []

for i in num:
    if i in dic:
        temp = dic.get(i)+1
        dic[i] = temp
    else:
        dic[i] = 1
        
result = sorted(dic.items(), key=lambda x: (-x[1], x[1]))

for i, j in result:
    answer += [i]*j
print(*answer)
