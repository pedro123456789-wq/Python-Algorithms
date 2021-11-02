def insertion_sort(array):
  for i in range(1, len(array)):
    current_value = array[i]
    
    while i > 0 and array[i - 1] > current_value:
        array[i] = array[i - 1]
        i -= 1
        
    array[i] = current_value

  return array


if __name__ == '__main__':
  test_array = [1, 10, 11, 7, 2, 9, 4]
  print(insertion_sort(test_array))
    
