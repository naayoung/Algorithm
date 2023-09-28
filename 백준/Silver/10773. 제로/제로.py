k = int(input())
num = []

for i in range(k):
    j = int(input())
    if(j != 0):
        num.append(j)
    else:
        del num[len(num)-1]
print(sum(num))
