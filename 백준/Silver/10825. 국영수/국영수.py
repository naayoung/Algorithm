import sys
input = sys.stdin.readline

n = int(input())
stu = [list(map(str, input().split())) for _ in range(n)]

for i in stu:
    for j in range(1, 4):
        i[j] = int(i[j])

answer = sorted(stu, key=lambda x: [-x[1], x[2], -x[3], x[0]])

for i in answer:
    print(i[0])