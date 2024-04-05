import sys
input = sys.stdin.readline

sen = input().rstrip()
w = input().rstrip()

count = 0
index = 0
for i in range(len(sen)):
    if index > i:
        continue
    if sen[i:i+len(w)] == w:
        count += 1
        index = i+len(w)
print(count)