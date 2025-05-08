import sys
input = sys.stdin.readline

letter = ['a', 'e', 'i', 'o', 'u', 'y']
while True:
    n = int(input().strip())
    ans = ''
    cnt = 0
    if n == 0:
        break
    else:
        for _ in range(n):
            word = input().strip()
            temp = 0

            for w in range(1, len(word)):
                if word[w] in letter and word[w-1] in letter:
                    if word[w] == word[w-1]:
                        temp += 1
            if temp >= cnt:
                cnt = temp
                ans = word
        print(ans)