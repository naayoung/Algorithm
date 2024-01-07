def solution(phone_book):
    answer = True
    dic = {}
    for nums in phone_book:
        dic[nums] = 1
    for nums in phone_book:
        temp = ""
        for num in nums:
            temp += num
            if temp in dic and temp != nums:
                answer = False
    return answer