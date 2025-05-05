import sys
input = sys.stdin.readline

T = int(input().strip())

masses = {
    'C': 12.01,
    'H': 1.008,
    'O': 16.00,
    'N': 14.01
}

for _ in range(T):
    formula = input().strip()
    total = 0
    i = 0

    while i < len(formula):
        if formula[i].isalpha():
            element = formula[i]
            i += 1
            count = ""

            while i < len(formula) and formula[i].isdigit():
                count += formula[i]
                i += 1

            if count == "":
                count = 1
            else:
                count = int(count)

            total += masses[element] * count

    print(f"{total:.3f}")