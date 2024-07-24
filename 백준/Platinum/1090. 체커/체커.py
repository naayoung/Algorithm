import sys
input = sys.stdin.readline

n = int(input().strip())
num = []
x_num, y_num = [], []
for _ in range(n):
    x, y = map(int, input().split())
    num.append((x, y))
    x_num.append(x)
    y_num.append(y)
answer = [-1] * n

for x in x_num:
    for y in y_num:
        distance = []
        for num_x, num_y in num:
            d = abs(num_x - x) + abs(num_y - y)
            distance.append(d)
        distance.sort()

        temp = 0
        for i in range(len(distance)):
            d = distance[i]
            temp += d
            if answer[i] == -1:
                answer[i] = temp
            else:
                answer[i] = min(temp, answer[i])

print(*answer)