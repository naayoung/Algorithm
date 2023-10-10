import sys, itertools
input = sys.stdin.readline
cm = []

for i in range(9):
    cm.append(int(input().strip()))
cm.sort()

answer = list(itertools.combinations(cm, 7))

for i in answer:
    if sum(i) == 100:
        print(*i,sep='\n')
        break