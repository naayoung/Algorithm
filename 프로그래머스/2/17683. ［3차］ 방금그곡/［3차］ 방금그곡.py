def normalize(s):
    return (s.replace("C#", "c")
             .replace("D#", "d")
             .replace("F#", "f")
             .replace("G#", "g")
             .replace("A#", "a")
             .replace("B#", "b"))

def get_info(info, time_len):
    if not info:
        return ""
    L = len(info)
    t, a = divmod(time_len, L)
    return info * t + info[:a]

def get_time(t1, t2):
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    return (h2 * 60 + m2) - (h1 * 60 + m1)

def solution(m, musicinfos):
    m = normalize(m)
    answer = '(None)'
    records = []

    for row in musicinfos:
        start, end, title, info = row.split(',')
        play_time = get_time(start, end)
        played = get_info(normalize(info), play_time)
        records.append((play_time, title, played))
    
    records.sort(key = lambda x:-x[0])

    for record in records:
        if m in record[2]:
            answer = record[1]
            break
    return answer