num = []

while True:
    n = int(input())
    if(n == 0):
        break
    else:
        num.append(n)

for i in num:
    i = str(i)
    if(i == ''.join(reversed(i))):
        print("yes")
    else:
        print("no")