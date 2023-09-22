import sys
sys.setrecursionlimit(10**7)

answer = 0

def solution(a, b, n):
    global answer
    
    if(n < a):
        return answer
    else:
        answer += (n//a)*b
        n = (n//a)*b+n%a
        return solution(a, b, n)
