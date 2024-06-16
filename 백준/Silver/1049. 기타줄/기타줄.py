import sys
input = sys.stdin.readline

n, m = map(int, input().split())
package, single = [], []
price = 0

for _ in range(m):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

while n > 0:
    if n >= 6:
        if n//6 * min(package) < n//6 * 6 * min(single):
            price += n//6 * min(package)
        else:
            price += n//6 * 6 * min(single)
        n -= n//6 * 6
    else:
        if min(package) > n * min(single):
            price += n * min(single)
        else:
            price += min(package)
        n = 0
print(price)