def solution(bandage, health, attacks):
    answer = 0
    
    #기술
    t, x, y = bandage[0], bandage[1], bandage[2]
    #시간
    time = 0
    #연속성공시간
    s = 0
    #최대 체력
    max_health = health
    #공격 횟수
    attack_t = 0
    
    for time in range(1, attacks[-1][0]+1):
        if time == attacks[attack_t][0]:
            s = 0
            health -= attacks[attack_t][1]
            attack_t += 1
        else:
            if max_health > health:
                health += x
                s += 1
                if s == t:
                    health += y
                    s = 0
                    
            if max_health < health:
                health = max_health
                
        if health <= 0:
            answer = -1
            break
        else:
            answer = health
                
    return answer