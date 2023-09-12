def solution(sides):
    answer = 0
    max_sides = max(sides)
    sides.remove(max_sides)
    if(max_sides < sum(sides)):
        answer = 1
    else:
        answer = 2
    return answer