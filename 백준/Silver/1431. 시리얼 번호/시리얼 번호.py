import sys
input = sys.stdin.readline

def sum_num(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result

N = int(input())
number = []
for _ in range(N):
    number.append(input().strip())

number.sort(key=lambda x:(len(x), sum_num(x), x))

for i in number:
    print(i)
