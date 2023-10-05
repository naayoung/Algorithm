case = int(input())

for i in range(case):
    n = int(input())
    clothes = {}

    for j in range(n):
        key, value = str(input()).split()

        if value not in clothes.keys():
            clothes[value] = 1
        else:
            clothes[value] += 1
    
    answer = 1
    for j in clothes:
        answer *= (clothes[j]+1)
    print(answer - 1)