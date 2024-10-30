import sys
input = sys.stdin.readline

s = int(input().strip())
switch = list(map(int, input().split()))
stu = int(input().strip())
for _ in range(stu):
    ss, num = map(int, input().split())

    #남학생
    if ss == 1:
        for i in range(num-1, s, num):
            switch[i] = 1 - switch[i]
    #여학생
    if ss == 2:
        # 여학생은 자신을 중심으로 대칭인 구간을 확인하며 변경
        num -= 1  # 인덱스를 0부터 시작하도록 조정
        left = right = num
        while left >= 0 and right < s and switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            if left != right:
                switch[right] = 1 - switch[right]
            left -= 1
            right += 1

for i in range(0, s, 20):
    print(*switch[i:i+20])
