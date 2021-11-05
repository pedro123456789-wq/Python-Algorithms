def linear_search(array, target):
    index, counter, found = -1, 0, False


    while not found and counter < len(array):
        if array[counter] == target:
            found = True
            index = counter
            break

        counter += 1

    return index



if __name__ == '__main__':
    test_array = [1, 5, 8, 10, 2]
    print(linear_search(test_array, 2))
