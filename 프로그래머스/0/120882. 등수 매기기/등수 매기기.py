def solution(score):
    answer = []
    avg = []
    for i in score:
        t = (i[0]+i[1])/2
        avg.append(t)

    temp = avg[:]
    temp.sort(reverse=True)
    
    for i in avg:
        t = temp.index(i)+1
        answer.append(t)
    return answer