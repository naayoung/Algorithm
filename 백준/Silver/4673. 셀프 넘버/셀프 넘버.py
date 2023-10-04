def d(n):
    total = 0
    total += n
    for i in range(0, len(str(n))):
        total += int(n/10**i)%10
    return total
 
tc = []
for i in range(10000):
    tc.append(d(i))
 
for j in range(10000):
    if j in tc:
        pass
    else:
        print(j)