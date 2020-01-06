def function_b(y, epsilon = 10**(-5)):
    num = y
    upper_band = y
    lower_band = 0
    while upper_band - lower_band >= epsilon:
        if num**2 > y:
            upper_band = num
        elif num**2 < y:
            lower_band = num
        else:
            return num

        num = (lower_band + upper_band)/2

    return num

print("%.4f" %function_b(8))