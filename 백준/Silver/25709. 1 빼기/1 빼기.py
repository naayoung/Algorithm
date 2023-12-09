import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0

while True:
    nn = list(str(n))

    if n == 0:
        print(count)
        break
    elif nn[0] == '0':
        nn.remove('0')
    elif '1' in nn:
        nn.remove('1')
        count += 1
        if len(nn) != 0:
            n = int(''.join(nn))
        else:
            n = n-1
    else:
        n = n-1
        count += 1