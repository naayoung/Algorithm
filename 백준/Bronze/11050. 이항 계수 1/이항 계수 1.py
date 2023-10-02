def factorial(x):
    result = 1
    for i in range(2, x+1):
        result *= i
    return result

n, k = map(int, input().split())
print(int(factorial(n) / (factorial(n-k)*factorial(k))))