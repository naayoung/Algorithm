import sys
input = sys.stdin.readline

original = 'abcdefghijklmnopqrstuvwxyz'
encoded = 'nopqrstuvwxyzabcdefghijklm'


def encode(w):
    temp = ''
    t = 0
    for word in w:
        t = original.find(word)
        temp += encoded[t]
    return temp

n = int(input().strip())
original_word = []
encoded_word = []
ans = 0
for _ in range(n):
    w = input().strip()
    original_word.append(w)
    encoded_word.append(encode(w))

original_word = set(original_word)
encoded_word = set(encoded_word)
for word in encoded_word:
    if word in original_word:
        ans += 1
print(ans)