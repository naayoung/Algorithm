import sys
from decimal import Decimal, getcontext
input = sys.stdin.readline

getcontext().prec = 50  # 충분한 정밀도

def parse_a(token):
    # "x"면 계수 1
    if token == "x":
        return 1
    # "0x", "123x" 같은 형태
    return int(token[:-1])

def format_truncate(val: Decimal) -> str:
    # Decimal → 문자열 변환 후 6자리 절삭
    s = format(val, 'f')  # 지수표기 방지
    if '.' not in s:
        # 정수라면 .000000 붙이기
        s = s + ".000000"
    else:
        front, back = s.split('.')
        back = (back + "000000")[:6]  # 6자리 절삭 (부족하면 0 채우기)
        s = front + "." + back
    # -0.000000 → 0.000000 처리
    if s.startswith("-0.000000"):
        s = "0.000000"
    return s

P = int(input())
for case_num in range(1, P + 1):
    eq = input().strip().split()  # ["ax", "+", "b", "=", "c"]
    a = parse_a(eq[0])
    b = int(eq[2])
    c = int(eq[4])

    print(f"Equation {case_num}")
    if a == 0:
        if c - b == 0:
            print("More than one solution.")
        else:
            print("No solution.")
    else:
        res = Decimal(c - b) / Decimal(a)
        print("x = " + format_truncate(res))
    if case_num != P:
        print()
