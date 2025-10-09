import sys
input = sys.stdin.readline

minguk = list(map(int, input().split()))
manse = list(map(int, input().split()))

minguk = sum(minguk)
manse = sum(manse)

print(max(minguk, manse))