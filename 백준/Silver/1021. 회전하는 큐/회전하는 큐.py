import sys, collections
input = sys.stdin.readline

n, m = map(int,input().split())
choice = list(map(int, input().split()))

q = collections.deque([_ for _ in range(1, n+1)])
count = 0

while len(choice) > 0:
    if choice[0] == q[0]:
        q.popleft()
        choice.remove(choice[0])
    elif q.index(choice[0]) < len(q)/2:
        q.rotate(-1)
        count += 1
    else:
        q.rotate(1)
        count += 1
print(count)