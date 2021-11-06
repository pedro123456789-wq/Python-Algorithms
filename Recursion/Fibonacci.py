def fibb(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
        
    return fibb(number - 1) + fibb(number - 2)
    

if __name__ == "__main__":
    print(permutations("abc"))
    print(summation_options(10))
    print(fibb(5))
