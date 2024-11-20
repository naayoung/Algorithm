def solution(survey, choices):
    answer = ''
    #[라이언형(R), 튜브형(T)], [콘형(C), 프로도형(F)], [제이지형(J), 무지형(M)], [어피치형(A), 네오형(N)]
    g = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        #동의
        if choices[i] > 4:
            g[survey[i][1]] += choices[i]-4
        #비동의
        if choices[i] < 4:    
            g[survey[i][0]] += 4-choices[i]
    g = list(g.items())

    for i in range(0, 8, 2):
        if g[i][1] >= g[i+1][1]:
            answer += g[i][0]
        if g[i][1] < g[i+1][1]:
            answer += g[i+1][0]
    return answer