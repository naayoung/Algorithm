import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    pair = 0

    A_count, B_count = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    for i in range(A_count):
        while True:
            if count == B_count or A[i] <= B[count]:
                pair += count
                break
            else:
                count += 1
    print(pair)