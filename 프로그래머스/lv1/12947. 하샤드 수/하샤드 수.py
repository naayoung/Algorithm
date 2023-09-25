def solution(x):
    x_sum = 0
    for i in str(x):
        x_sum += int(i)
  
    #i = x//10
    #x_sum = x//(10*i) + x%(10*i)
    
    if x % x_sum == 0:
        return True
    else:
        return False
    