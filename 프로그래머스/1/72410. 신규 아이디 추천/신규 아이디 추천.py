def stage1(id):
    return id.lower()

def stage2(id):
    temp = ''
    for i in id:
        if i=='-' or i=='_' or i=='.' or i.isdigit() or i.isalpha():
            temp += i
    return temp

def stage3(id):
    while '..' in id:
        id = id.replace('..', '.')
    return id

def stage4(id):
    return id.strip('.')

def stage5(id):
    temp = id
    if len(id) == 0:
        temp = 'a'
    return temp

def stage6(id):
    id = id[:15]
    return id.rstrip('.')

def stage7(id):
    while len(id) < 3:
        id += id[-1]
    return id

def stage(new_id):
    new_id = stage1(new_id)
    new_id = stage2(new_id)
    new_id = stage3(new_id)
    new_id = stage4(new_id)
    new_id = stage5(new_id)
    new_id = stage6(new_id)
    new_id = stage7(new_id)
    return new_id
    
def solution(new_id):
    answer = stage(new_id)
    return answer