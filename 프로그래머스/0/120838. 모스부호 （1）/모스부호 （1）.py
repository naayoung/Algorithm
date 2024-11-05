def solution(letter):
    answer = ''
    mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    letter = list(letter.split())
    
    for i in letter:
        t = mos.index(i)+97
        answer += chr(t)
    return answer