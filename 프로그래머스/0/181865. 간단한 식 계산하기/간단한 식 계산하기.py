def solution(binomial):
    answer = 0
    binomial = list(binomial.split())
    print(binomial)
    
    if binomial[1] == '+':
        answer = int(binomial[0]) + int(binomial[2])
    elif binomial[1] == '-':
        answer = int(binomial[0]) - int(binomial[2])
    elif binomial[1] == '*':
        answer = int(binomial[0]) * int(binomial[2])
    return answer