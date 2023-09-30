n = int(input())
num = []

for i in range(n):
    member = list(map(str, input().split()))
    num.append(member)

num.sort(key = lambda x : int(x[0]))

for i in num:
    print(' '.join(i))