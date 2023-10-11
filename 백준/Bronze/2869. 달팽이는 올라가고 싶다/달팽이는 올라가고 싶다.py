import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
answer = (v-a)//(a-b)

while answer*(a-b)+b < v:
    answer += 1

print(answer)