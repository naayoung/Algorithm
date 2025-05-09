import sys
input = sys.stdin.readline

def cal_time(t):
    hh, mm = t.split(':')
    hh, mm = int(hh)%12, int(mm)
    hh_degree, mm_degree = hh*30+mm*0.5, mm*6

    time = abs(hh_degree-mm_degree)

    return min(time, 360-time)

T = int(input().strip())
for _ in range(T):
    times = list(input().split())
    angles = []

    for t in times:
        angle = cal_time(t)
        angles.append((angle, t))
    
    angles.sort()
    print(angles[2][1])