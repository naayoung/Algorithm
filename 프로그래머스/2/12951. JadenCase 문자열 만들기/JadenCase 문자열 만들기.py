def solution(s):
    answer = s[0].upper()
    s = s.lower()
    for i in range(1, len(s)):
        temp = s[i]
        if s[i-1] == " ":
            temp = temp.upper()
            
        answer += temp
    return answer