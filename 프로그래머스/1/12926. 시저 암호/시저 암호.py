def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif 'a' <= i <= 'z':  # 소문자일 경우
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= i <= 'Z':  # 대문자일 경우
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    return answer