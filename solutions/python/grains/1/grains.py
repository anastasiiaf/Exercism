def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        grain = 0
        step = 1
        while step <= number:
            if step == 1:
                grain = 1
            else:
                grain = grain * 2
            step += 1
    return grain



def total():
    i = 1
    total_grain = 0
    while i <= 64:
        total_grain += square(i)
        i += 1
    return total_grain

