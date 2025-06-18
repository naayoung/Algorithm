import sys
input = sys.stdin.readline

def normalize(snow):
    rotations = []
    # 회전
    for i in range(6):
        rotations.append(tuple(snow[i:] + snow[:i]))
    # 뒤집어서 회전
    reversed_snow = snow[::-1]
    for i in range(6):
        rotations.append(tuple(reversed_snow[i:] + reversed_snow[:i]))
    return min(rotations)

n = int(input())
seen = set()
found = False

for _ in range(n):
    snow = list(map(int, input().split()))
    key = normalize(snow)
    if key in seen:
        found = True
        break
    seen.add(key)

print("Twin snowflakes found." if found else "No two snowflakes are alike.")