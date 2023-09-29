n = int(input())
testcase = [str(input()) for i in range(n)]

for i in testcase:
    count = 0
    answer = 0
    for j in i:
        if(j == "O"):
            count += 1
            answer += count
        else:
            count = 0
    print(answer)