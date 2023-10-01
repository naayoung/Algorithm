n, k = map(int, input().split())

num = [True] * (n+1)
count = []

for i in range(2, n+1):
    if(num[i]):
        num[i] = False
        count.append(i)
        for j in range(i+i, n+1, i):
            num[j] = False
            if(j not in count):
                count.append(j)
print(count[k-1])