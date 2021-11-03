def binary_search(array, target, starting_index, ending_index):
    if ending_index < starting_index:
        return -1

    middle_index = (starting_index + ending_index) // 2

    if array[middle_index] == target:
        return middle_index
    elif array[middle_index] < target:
        return searching_algos.binary_search(array, target, middle_index + 1, ending_index)
    elif array[middle_index] > target:
        return searching_algos.binary_search(array, target, starting_index, middle_index - 1)



if __name__ == '__main__':
    test_array = [1, 2, 4, 6, 8]
    print(binary_search(test_array, 8, 0, len(test_array)))
