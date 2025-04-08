import sys
input = sys.stdin.readline

m = list(input().strip())
cnt = 0
temp = []

for i in range(len(m)):
    if m[i] == '(':  # 여는 괄호면 스택에 추가
        temp.append('(')
    else:  # 닫는 괄호일 때
        temp.pop()
        if m[i - 1] == '(':  # 레이저
            cnt += len(temp)
        else:  # 막대기 끝
            cnt += 1
print(cnt)