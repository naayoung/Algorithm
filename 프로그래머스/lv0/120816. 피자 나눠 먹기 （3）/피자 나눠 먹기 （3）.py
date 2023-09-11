def solution(slice, n):
    pizza = 1
    
    while(slice * pizza / n < 1):
        pizza += 1 
    return pizza