import sys
from decimal import Decimal, getcontext
input = sys.stdin.readline

getcontext().prec = 50  # 충분한 정밀도

n = int(input().strip())
for t in range(n):
    parts = input().split()
    a_str, b_str, c_str = parts[0], parts[2], parts[4]

    # a 구하기
    if a_str == "x":
        a = 1
    else:
        a = int(a_str[:-1])   # 마지막 'x' 제외

    b = int(b_str)
    c = int(c_str)

    print(f"Equation {t+1}")
    if a == 0:
        # ax가 없는 경우
        if c - b == 0:
            print("More than one solution.")
        else:
            print("No solution.")
    else:
        # 해 구하기
        res = Decimal(c - b) / Decimal(a)
        s = format(res, 'f')  # 소수점 문자열로 변환 (지수표기 방지)

        if '.' not in s:
            s = s + ".000000"
        else:
            front, back = s.split('.')
            back = (back + "000000")[:6]  # 6자리로 자르기 (부족하면 0 채우기)
            s = front + "." + back

        if s.startswith("-0.000000"):
            s = "0.000000"

        print("x = " + s)

    if t != n-1:
        print()
