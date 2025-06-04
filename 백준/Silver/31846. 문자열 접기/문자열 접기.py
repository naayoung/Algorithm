import sys
input = sys.stdin.readline

N = int(input().strip())
S = input().strip()
Q = int(input().strip())
for _ in range(Q):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    temp = S[l:r+1]

    ans = 0
    for i in range(1, len(temp)):
        cnt = 0
        t1 = temp[0:i][::-1]
        t2 = temp[i:]

        if len(t1) <= len(t2):
            for j in range(len(t1)):
                if t1[j] == t2[j]:
                    cnt += 1
        else:
            for j in range(len(t2)):
                if t1[j] == t2[j]:
                    cnt += 1
        ans = max(ans, cnt)
    print(ans)