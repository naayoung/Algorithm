def solution(s):
    answer = []
    s = list(s.lower().split(' '))

    for i in s:
        if i == '':
            answer.append('')
        elif not i[0].isdigit():
            answer.append(i[0].upper() + i[1:])
        else:
            answer.append(i)
    
    answer = ' '.join(answer)
            
    return answer