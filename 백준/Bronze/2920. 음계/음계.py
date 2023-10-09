import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
answer = []
count = 0

for i in range(1, 8):
    if num[i-1] + 1 == num[i]:
        count += 1
    elif num[i-1] - 1 == num[i]:
        count -= 1
    else:
        count = 0

if count == 7:
    print("ascending")
elif count == -7:
    print("descending")
else:
    print("mixed")