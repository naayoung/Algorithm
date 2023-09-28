a, b = map(int, input().split())
answer1 = 0
answer2 = 0

if(a >= b):
    n = a
else:
    n = b

for i in range(0, n+1):
    if(i == 0):
        answer1 = 0
        answer2 = 0
    elif(a%i == 0 and b%i == 0):
        answer1 = i
        answer2 = a//answer1 * b//answer1 * answer1
print(answer1)
print(answer2)