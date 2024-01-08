def solution(genres, plays):
    total = {}
    gen_dic = {}
    answer = []
    
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
            gen_dic[genres[i]].append((plays[i], i))
        else:
            total[genres[i]] = plays[i]
            gen_dic[genres[i]] = [(plays[i], i)]
            
    total = sorted(total.items(), key=lambda x:x[1], reverse=True)
    
    for i in total:
        play = gen_dic[i[0]]
        play = sorted(play, key=lambda x:x[0], reverse=True)
        
        for item in play[:2]:
            answer.append(item[1])
    return answer