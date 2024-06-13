import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    testcase = list(map(str, input().split()))

    while True:
        animal = list(map(str, input().split()))

        if animal[0] == "what":
            print(*testcase)
            break

        while animal[2] in testcase:
            testcase.remove(animal[2])