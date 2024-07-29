import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

select_nums = []

def find_nums(count, start):
    if count == m:
        print(*select_nums)
        return
    
    last_num = -1
    for i in range(start, n):
        if nums[i] != last_num:  # 중복된 숫자를 선택하지 않음
            select_nums.append(nums[i])
            find_nums(count + 1, i + 1)  # 오름차순 유지 위해 start를 i + 1로 설정
            select_nums.pop()
            last_num = nums[i]  # 마지막으로 선택된 숫자 기록

find_nums(0, 0)