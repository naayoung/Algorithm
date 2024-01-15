def solution(strings, n):
    answer = []
    temp = {}
    for i in strings:
        temp[i] = str(i[n])
    temp_list = dict(sorted(temp.items(), key=lambda x:(x[1], x[0]), reverse=False))
    answer = list(temp_list.keys())
    return answer