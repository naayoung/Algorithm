trout = int(input())
pike = int(input())
pickerel = int(input())
total = int(input())

num = []
for x in range(total+1):
    for y in range(total+1):
        for z in range(total+1):
            if x*trout + y*pike + z*pickerel <= total and x*trout + y*pike + z*pickerel > 0:
                num.append((x, y, z))

num.sort(key = lambda x:(x[0] == 0, x[1] == 0, x[0], x[1], x[2]))
for x, y, z in num:
    print(x,'Brown Trout,',y,'Northern Pike,',z,'Yellow Pickerel')
print('Number of ways to catch fish:', len(num))