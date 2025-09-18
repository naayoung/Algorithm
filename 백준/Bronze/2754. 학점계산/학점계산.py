import sys
input = sys.stdin.readline

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-','C+', 'C0', 'C-', 'D+', 'D0', 'D-', 'F']
score2 = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]

s = input().strip()
temp = score.index(s)
print(score2[temp])