import sys
input = sys.stdin.readline

def check(color):
    cnt = 1
    before = ''
    for i in s:
        if i != color:
            if i != before:
                cnt += 1
        before = i
    return cnt

n = int(input().strip())
s = list(input().strip())

print(min(check('B'), check('R')))