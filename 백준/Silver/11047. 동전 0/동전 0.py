n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
num.sort(reverse=True)
count = 0

for i in num:
    if(i <= k):
        count += k//i
        k = k%i
print(count)