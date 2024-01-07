def solution(nums):
    temp = {}
    for num in nums:
        if num in temp:
             temp[num] += 1
        else:
            temp[num] = 1
    answer = min(len(temp), sum(temp.values())//2)
    return answer