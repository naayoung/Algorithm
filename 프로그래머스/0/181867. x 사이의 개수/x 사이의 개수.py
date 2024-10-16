def solution(myString):
    answer = []
    myString = list(myString.split('x'))
    for i in myString:
        answer.append(len(i))
    return answer