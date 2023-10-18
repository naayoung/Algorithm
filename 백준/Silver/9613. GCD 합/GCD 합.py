import sys, math, itertools
input = sys.stdin.readline

t = int(input())
num = [list(map(int, input().split())) for _ in range(t)]
answer = []

def combi(n):
    combi = []
    temp2 = []
    combi = list(itertools.combinations(n, 2))
    for i in combi:
        i = list((i))
        a, b = i[0], i[1]
        temp2.append(math.gcd(a, b))
    answer.append(sum(temp2))
for i in num:
    temp = []
    for j in range(1, i[0]+1):
        temp.append(i[j])
    combi(temp)
print(*answer, sep='\n')
