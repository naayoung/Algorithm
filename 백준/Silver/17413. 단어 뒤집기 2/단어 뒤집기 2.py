import sys
input = sys.stdin.readline

S = input().strip()
temp = ''
ans = ''
in_tag = False

for s in S:
    if s == '<':
        ans += temp[::-1]
        temp = ''
        in_tag = True
        ans += s
    elif s == '>':
        in_tag = False
        ans += s
    elif in_tag:
        ans += s
    elif s == ' ':
        ans += temp[::-1] + ' '
        temp = ''
    else:
        temp += s
ans += temp[::-1]
print(ans)