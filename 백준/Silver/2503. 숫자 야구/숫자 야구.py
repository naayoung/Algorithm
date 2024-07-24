import sys
input = sys.stdin.readline

n = int(input().strip())
hint = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a != b and b != c and a != c:
                count = 0
                for number, strike_hint, ball_hint in hint:
                    strike, ball = 0, 0
                    a_hint, b_hint, c_hint = map(int, str(number))

                    if a == a_hint: strike += 1
                    if b == b_hint: strike += 1
                    if c == c_hint: strike += 1
                    
                    if a == b_hint or a == c_hint: ball += 1
                    if b == a_hint or b == c_hint: ball += 1
                    if c == a_hint or c == b_hint: ball += 1

                    if strike == strike_hint and ball == ball_hint:
                        count += 1
                if count == n:
                    answer += 1
print(answer)