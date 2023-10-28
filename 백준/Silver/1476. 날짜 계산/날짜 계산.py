import sys
input = sys.stdin.readline

e,s,m = map(int, input().split())
answer = 1

while True:
    if answer % 15 == e % 15 and answer % 28 == s % 28 and answer % 19 == m % 19:
        print(answer)
        break
    else:
        answer += 1