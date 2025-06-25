import sys
input = sys.stdin.readline

poem = input().rstrip('\n')
space = int(input().strip())
alpha = list(map(int, input().split()))

# 1. 본문 내용 누름
prev = ''
for ch in poem:
    if ch == prev:
        continue
    if ch == ' ':
        space -= 1
        if space < 0:
            print(-1)
            sys.exit()
    elif ch.isalpha():
        idx = ord(ch.lower()) - ord('a')
        alpha[idx] -= 1
        if alpha[idx] < 0:
            print(-1)
            sys.exit()
    prev = ch

# 2. 제목 추출
# 단어 경계(첫 글자) 추출: 맨 앞 또는 앞이 공백일 때 대문자로
title = ''.join(poem[i].upper() for i in range(len(poem)) 
                if poem[i].isalpha() and (i == 0 or poem[i-1] == ' '))

# 3. 제목 누름
prev = ''
for ch in title:
    if ch == prev:
        continue
    idx = ord(ch.lower()) - ord('a')
    alpha[idx] -= 1
    if alpha[idx] < 0:
        print(-1)
        sys.exit()
    prev = ch

# 4. 공백 사용 제한은 이미 본문에서만 감소 → 제목엔 공백 없음
print(title)
