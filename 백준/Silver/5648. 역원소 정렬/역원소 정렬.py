import sys
input = sys.stdin.read

#Python에서 *을 붙여서 변수를 선언해주면 정해지지 않은 개수의 입력값이 들어온다는 의미
n, *num = input().split()

for i in range(int(n)):
    num[i] = num[i][::-1]

num = list(map(int, num))
print(*sorted(num), sep="\n")