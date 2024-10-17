def solution(answers):
    answer = []
    nums = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    find = []

    for n in range(3):
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == nums[n][i % len(nums[n])]:
                cnt += 1
        find.append(cnt)
    
    max_find = max(find)
    for i in range(3):
        if find[i] == max_find:
            answer.append(i+1)
    
    return answer