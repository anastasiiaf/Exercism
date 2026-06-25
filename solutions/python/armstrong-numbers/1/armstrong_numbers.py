def is_armstrong_number(number):
    digit = number % 10
    sum = 0
    num_digits = len(str(number))
    i=1

    while i <= num_digits:
        
        digit =  (number % (10**i)) // (10**(i-1))
        sum = sum + digit**num_digits
        print(digit, i, sum)
        i+=1
    return sum==number