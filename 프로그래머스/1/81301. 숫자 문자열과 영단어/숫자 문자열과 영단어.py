def solution(s):
    answer = ''
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(10):
        if number[i] in s:
            s = s.replace(number[i], str(i)) 
    answer = int(s)
    return answer