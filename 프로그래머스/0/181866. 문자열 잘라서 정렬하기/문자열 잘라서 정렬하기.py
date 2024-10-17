def solution(myString):
    answer = []
    answer = myString.split('x')
    
    while True:
        if "" in answer:
            answer.remove("")
        else:
            break
    answer.sort()
    return answer