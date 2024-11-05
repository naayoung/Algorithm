def solution(polynomial):
    answer = ''
    polynomial = list(polynomial.split())
    
    t1 = 0
    t2 = 0
    for p in polynomial:
        if 'x' in p:
            if len(p) >= 2:
                t1 += int(p[0:len(p)-1])
            else:
                t1 += 1
        elif p != '+':
            t2 += int(p)
        
    if t1 == 0:
        t1 = ''
    elif t1 == 1:
        t1 = 'x'
    else:
        t1 = str(t1)+'x'

    t2 = str(t2)
    
    if t1 == '':
        answer = t2
    elif int(t2) != 0:
        answer = t1 + ' + ' + t2
    else:
        answer = t1
    
    return answer