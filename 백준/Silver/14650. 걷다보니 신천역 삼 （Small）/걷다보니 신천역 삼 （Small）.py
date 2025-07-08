import sys
input = sys.stdin.readline

def confirm_num(list):
    num = 0
    for i in range(n):
        num += list[i]*(10**(n-i-1))
    if num%3 == 0:
        if num not in visited:
            visited.append(num)
            return True
    return False

def backtrack():
    if len(num) != 0 and num[0] == 0:
        return
    if len(num) == n:
        global cnt
        if confirm_num(num):
            cnt += 1
        return
    
    for i in temp:
        num.append(i)
        backtrack()
        num.pop()
    
n = int(input().strip())
temp = [0, 1, 2]
num = []
visited = []
cnt = 0

backtrack()
print(cnt)