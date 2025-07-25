import sys
input = sys.stdin.readline

n = int(input().strip())
num = list(map(int, input().split()))
pro = [_ for _ in range(1, n+1)] #현재 남아있는

professor = 1 #현재 교수 번호
for _ in range(n-1):
    number = num[professor-1] #교수가 선택한 번호
    target = number%len(pro)-1 #삭제할 값

    offset = pro.index(professor)
    pro = pro[offset:] + pro[:offset]

    professor = pro[target+1] #다음 시작 교수
    pro.pop(target)


print(*pro)