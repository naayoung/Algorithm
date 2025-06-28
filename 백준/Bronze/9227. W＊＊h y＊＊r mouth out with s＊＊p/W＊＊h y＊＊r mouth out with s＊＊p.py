import sys
input = sys.stdin.readline

dic = set()
while True:
    line = input().strip()
    if line == '##':
        break
    dic.add(line)

while True:
    line = input().strip()
    if line.strip() == '#':
        break

    chars = list(line)
    i = 0
    while i + 3 < len(line):
        word = line[i:i+4]
        if word.isalpha():
            start = word[0]
            end = word[3]
            if start + end in dic:
                chars[i+1] = '*'
                chars[i+2] = '*'
                i += 4
                continue
        i += 1
    print("".join(chars))
