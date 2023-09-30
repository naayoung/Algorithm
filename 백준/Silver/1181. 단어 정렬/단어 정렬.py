import sys
input = sys.stdin.readline

n = int(input())
word = [str(input()) for _ in range(n)]

word = sorted(set(word))
word.sort(key = len)

for i in word:
    print(i.strip())