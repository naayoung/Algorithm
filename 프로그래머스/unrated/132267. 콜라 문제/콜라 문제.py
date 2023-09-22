import sys
sys.setrecursionlimit(10**7)

answer = 0
count = 0

def solution(a, b, n):
    global answer
    global count
    
    if(n < a):
        """if(b > 1):
            answer = answer*(count-1)*b"""
        return answer
    else:
        answer += (n//a)*b
        n = (n//a)*b+n%a
        count += 1
        return solution(a, b, n)
