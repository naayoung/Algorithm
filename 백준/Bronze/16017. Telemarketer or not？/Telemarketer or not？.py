import sys
input = sys.stdin.readline

ans = "ignore"
for i in range(4):
    num = int(input().strip())

    if i == 0 or i == 3:
        if num == 8 or num == 9:
            continue
        else:
            ans = "answer"
    else:
        if i == 1:
            temp = num
        else:
            if num != temp:
                ans = "answer"
print(ans)
