def solution(myString):
    answer = ''
    myString = myString.lower()
    for s in myString:
        if s == 'a':
            answer += 'A'
        else:
            answer += s
    return answer