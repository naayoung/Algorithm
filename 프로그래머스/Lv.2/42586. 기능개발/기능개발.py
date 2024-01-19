import math
def solution(progresses, speeds):
    answer = {}
    per = 0
    
    for i in range(len(progresses)):
        per = math.ceil((100-progresses[i])/speeds[i])
        
        if len(answer) == 0:
            answer[per] = 1
        elif list(answer.keys())[-1] >= per:
            temp = list(answer.values())[-1]
            temp += 1
            answer[list(answer.keys())[-1]] = temp
        else:
            answer[per] = 1
    return list(answer.values())