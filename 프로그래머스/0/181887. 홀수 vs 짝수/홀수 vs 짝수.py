def solution(num_list):
    answer = 0
    temp1, temp2 = 0, 0
    for i in range(len(num_list)):
        #홀수
        if i%2 == 0:
            temp1 += num_list[i]
        #짝수
        else:
            temp2 += num_list[i]
    answer = max(temp1, temp2)
    return answer