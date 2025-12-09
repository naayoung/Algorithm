import sys
input = sys.stdin.readline

hh, mm = map(int, input().split())
ans = (hh-9)*60+mm
print(ans)