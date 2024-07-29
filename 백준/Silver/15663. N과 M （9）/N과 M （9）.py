import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

select_nums = []
used = [False] * n

def find_nums(count):
    if count == m:
        print(*select_nums)
        return
    
    last_num = -1  # 초기값 설정: nums에 없는 값
    for i in range(n):
        if not used[i] and nums[i] != last_num:
            used[i] = True
            select_nums.append(nums[i])
            find_nums(count + 1)
            select_nums.pop()
            used[i] = False
            last_num = nums[i]

find_nums(0)