num = []

while True:
    n= list(map(int, input().split()))
    if(sum(n) == 0):
        break
    else:
        num.append(n)
        n.sort()

for i in num:
    if(i[0]**2 + i[1]**2 == i[2]**2):
        print("right")
    else:
        print("wrong")