import sys
input = sys.stdin.readline

score = list(map(int, input().split()))

for i in range(20):
    if score[i] == 20:
        if i+1 < 20 and score[i-1] >= 0:
            Alice = score[i-1] + score[i] + score[i+1]
        elif i+1 >= 20:
            Alice = score[i-1] + score[i] + score[0]
        elif i-1 < 0:
            Alice = score[i-1] + score[i] + score[19]
Alice = Alice/3
Bob = sum(score)/20

if Alice > Bob:
    print("Alice")
elif Alice < Bob:
    print("Bob")
else:
    print("Tie")