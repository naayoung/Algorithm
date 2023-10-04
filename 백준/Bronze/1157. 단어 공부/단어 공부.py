import sys
input = sys.stdin.readline

word = str(input()).strip().upper()
ans = {}

for i in word:
    if i not in ans:
        count = 1
        ans[i] = count
    else:
        count = ans[i] + 1
        ans[i] = count

ans_values = list(ans.values())
ans = sorted(ans.items(), key = lambda x : x[1], reverse = True)
count = 0

for i in ans:
    if(max(ans_values) != i[1]):
        continue
    else:
        count += 1

if len(ans) == 1 or count == 1:
    print(ans[0][0])
else:
    print("?")