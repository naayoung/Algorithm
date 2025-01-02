def solution(a, b, c, d):
    answer = 0
    temp = [0]*6
    num = [a, b, c, d]
    for n in num:
        temp[n-1] += 1

    if 4 in temp:
        p = temp.index(4)+1
        answer = 1111*p
    elif 3 in temp:
        p = temp.index(3)+1
        q = temp.index(1)+1
        answer = (10*p+q)**2
    elif 2 in temp:
        tt = []
        if 1 in temp:
            for t in range(6):
                if temp[t] == 1:
                    tt.append(t+1)
            q, r = tt[0], tt[1]
            answer = q*r      
        else:
            for t in range(6):
                if temp[t] == 2:
                    tt.append(t+1)
            p, q = tt[0], tt[1]
            answer = (p+q)*abs(p-q) 
    else:
        answer = min(num)
        
    
    return answer