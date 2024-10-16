def solution(myString, pat):
    answer = 0
    myString, pat = myString.lower(), pat.lower()
    if pat in myString:
        answer = 1
    else:
        answer = 0
    return answer