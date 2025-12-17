import sys
input = sys.stdin.readline

n = int(input().strip())
timeline = []
for _ in range(n):
    hh, mm, ss = map(int, input().split())
    temp = (hh*60+mm)*60+ss
    timeline.append((hh, mm, ss, temp))

timeline.sort(key=lambda x: x[3])

for time in timeline:
    print(time[0], time[1], time[2])