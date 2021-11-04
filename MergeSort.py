from random import randint


def mergeSort(array):
    def sort_sections(first_half, second_half):
        sorted_array = []
        right_index, left_index = 0, 0 

        while left_index < len(first_half) and right_index < len(second_half):
            if first_half[left_index] < second_half[right_index]:
                sorted_array.append(first_half[left_index])
                left_index += 1

            else:
                sorted_array.append(second_half[right_index])
                right_index += 1


        if right_index < len(second_half):
            for i in range(right_index, len(second_half)):
                sorted_array.append(second_half[i])

        elif left_index < len(first_half):
            for i in range(left_index, len(first_half)):
                sorted_array.append(first_half[i])

        return sorted_array
    
    
    if len(array) == 1:
        return array

    mid_index = len(array) // 2
    first_half, second_half = array[:mid_index], array[mid_index:]

    return sort_sections(mergeSort(first_half), mergeSort(second_half))


        



if __name__ == '__main__':
    random_array = []
    
    for _ in range(10):
        random_number = randint(0, 100)

        if random_number not in random_array:
            random_array.append(random_number)

    
    print(random_array)
    print(mergeSort(random_array))
