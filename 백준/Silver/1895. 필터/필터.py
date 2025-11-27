import sys
input = sys.stdin.readline

R, C = map(int, input().split())
image = []
for _ in range(R):
    image.append(list(map(int, input().split())))
T = int(input().strip())

ans = 0
temp = []

for r in range(R-2):
    for c in range(C-2):
        temp = []

        for x in range(3):
            for y in range(3):
                temp.append(image[r+x][c+y])
        temp.sort()
        med = temp[4]

        if med >= T:
            ans += 1

print(ans)