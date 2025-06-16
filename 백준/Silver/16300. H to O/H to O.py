import sys
input = sys.stdin.readline

def parse_with_index(s, mult=1):
    d = dict()
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        if num == 0:
            num = 1  # 개수가 안 붙었으면 1개
        if ch not in d:
            d[ch] = 0
        d[ch] += num * mult
    return d

m, n = input().split()
nm = list(input().strip())
n = int(n)

m_dict = parse_with_index(m, mult=n)
nm_dict = parse_with_index(nm)

ans = float('inf')
for ch in nm_dict:
    if ch not in m_dict:
        ans = 0
        break
    ans = min(ans, m_dict[ch] // nm_dict[ch])

print(ans)