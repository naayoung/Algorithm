def solution(n):
    answer = 0
    nn = []
    temp = ''
    
    #3진법으로 변환(뒤집은 값)
    while True:
        if n < 3:
            nn.append(n)
            break
        nn.append(n%3)
        n = n//3
        
    for i in nn:
        temp += str(i)
    temp = list(temp)
    
    #10진법으로 표현
    for t in range(len(temp)):
        answer = answer*3 + int(temp[t])
    return answer