import sys
input = sys.stdin.readline

word1 = list(input().strip())
word2 = list(input().strip())

i = 0
while i < len(word1):
    if word1[i] in word2:
        word2.remove(word1[i])
        word1.remove(word1[i])
        i -= 1
    i += 1

print(len(word1) + len(word2))