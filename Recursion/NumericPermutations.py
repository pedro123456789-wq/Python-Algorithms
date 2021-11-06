def summation_options(number):
    if number == 1:
        return [[number]]
    elif number < 1:
        return None
    
    options = []
    
    for i in range(number, 0, -1):
        remaining = number - i
        sub_options = summation_options(remaining)
        
        if sub_options:
            for option in sub_options:
                options.append([i] + option)
        else:
            options.append([i])
            
    return options
        
        
if __name__ == "__main__":
    print(summation_options(10))
