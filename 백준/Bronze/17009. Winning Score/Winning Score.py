import sys
input = sys.stdin.readline

apple, banana = 0, 0
for i in range(3, 0, -1):
    temp = int(input().strip())
    apple += temp*i
for i in range(3, 0, -1):
    temp = int(input().strip())
    banana += temp*i

if apple > banana:
    print('A')
elif banana > apple:
    print('B')
else:
    print('T')