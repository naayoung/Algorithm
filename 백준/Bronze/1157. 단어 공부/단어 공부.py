import sys
input = sys.stdin.readline

word = str(input()).strip().upper()
word_list = list(set(word))
answer = []
count = 0

for i in word_list:
    answer.append(word.count(i))

for i in answer:
    if max(answer) == i:
        count += 1

if(count >= 2):
    print("?")
else:
    print(word_list[answer.index(max(answer))])