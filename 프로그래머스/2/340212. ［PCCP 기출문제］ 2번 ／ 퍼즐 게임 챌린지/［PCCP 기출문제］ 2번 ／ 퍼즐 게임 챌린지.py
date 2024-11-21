def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        level = (left + right) // 2
        time = times[0]
        
        for i in range(1, len(diffs)):
            time_cur = times[i]
            time_prev = times[i-1]
                
            if diffs[i] <= level:
                time += time_cur
            elif diffs[i] > level:
                time += (time_cur+time_prev)*(diffs[i] - level) + time_cur

        if time <= limit:
            answer = level
            right = level - 1
        else:
            left = level + 1           
    return answer