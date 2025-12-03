def is_armstrong_number(number):
    temp = number
    count = 0
    while temp > 0:
        temp //= 10
        count+=1

    total = 0
    temp = number
    for i in range (1,count+1):
        remainder = temp%10
        total += remainder**count
        temp //= 10

    return number == total 

    
