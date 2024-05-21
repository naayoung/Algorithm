import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [0, 1, 2]

if n < 3:
    print(arr[n])
else:
    for i in range(3, n+1):
        arr.append((arr[i-1] + arr[i-2]) % 10007)
    print(arr[n])