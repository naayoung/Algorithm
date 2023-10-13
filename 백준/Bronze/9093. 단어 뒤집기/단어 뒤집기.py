import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    answer = []
    sen = list(map(str, input().split()))
    
    for i in sen:
        answer.append(''.join(reversed(i)))
    print(*answer)