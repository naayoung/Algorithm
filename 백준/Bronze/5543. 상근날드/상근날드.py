import sys
input = sys.stdin.readline

hambuger = []
drink = []
for i in range(5):
    temp = int(input().strip())

    if i < 3:
        hambuger.append(temp)
    else:
        drink.append(temp)
        
print(min(hambuger)+min(drink)-50)