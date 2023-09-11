def solution(rsp):
    answer = []
    
    for r in rsp:
        if(r == "2"):
            answer.append("0")
        elif(r == "0"):
            answer.append("5")
        else:
            answer.append("2")
    return ''.join(answer)