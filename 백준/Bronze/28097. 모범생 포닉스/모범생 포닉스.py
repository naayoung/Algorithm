n = int(input())
t = list(map(int, input().split()))

if len(t) > 1:
    time = sum(t)+(n-1)*8
else:
    time = t[0]
d = time//24
print(d, time%24)