def str_to_int(time):
    #시간 초로 변환하는 함수
    mm, ss = time.split(':')
    mm, ss = int(mm), int(ss)
    time = mm*60+ss
    return time

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    #시간 초로 변환
    video_len_time = str_to_int(video_len)
    pos_time = str_to_int(pos)
    op_start_time = str_to_int(op_start)
    op_end_time = str_to_int(op_end)
    
    for command in commands:
        #오프닝 구간일 경우, 오프닝이 끝나는 위치로
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
        if command == 'prev':
            pos_time -= 10
            #10초 미만인 경우, 영상의 처음 위치로
            if pos_time < 0:
                pos_time = 0
        if command == 'next':
            pos_time += 10
            #남은 시간이 10초 미만인 경우, 영상의 마지막 위치로
            if pos_time > video_len_time:
                pos_time = video_len_time
        #오프닝 구간일 경우, 오프닝이 끝나는 위치로 재확인    
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
            
    mm, ss = str(pos_time//60), str(pos_time%60)
    if len(mm) == 1:
        mm = '0'+str(int(mm))
    if len(ss) == 1:
        ss = '0'+str(int(ss))
    answer = mm+':'+ss
    
    return answer