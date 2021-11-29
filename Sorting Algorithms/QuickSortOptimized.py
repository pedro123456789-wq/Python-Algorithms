#out-of-place, stable version
def quick_sort(array):
	if len(array) < 2:
		return array
  
  lower, equal, greater = [], [], []
  pivot = array[0]
  
  for element in array:
    if element > pivot:
      greater.append(element)
    elif element < pivot:
      lower.append(element)
    else:
      equal.append(element)


	return quick_sort(lower) + equal + quick_sort(greater)

	

#inplace, unstable version
def quick_sort_v2(array):
	def inplace_sort(start_index, end_index):
		if start_index < end_index:
			pivot_index = randint(start_index, end_index)
			pivot = array[pivot_index]
			array[start_index], array[pivot_index] = array[start_index], array[pivot_index]
			lower_index = start_index + 1

			for greater_index in range(lower_index, end_index):
				if array[greater_index] < pivot:
					array[lower_index], array[greater_index] = array[greater_index], array[lower_index]
					lower_index += 1

			array[lower_index - 1], array[start_index] = array[start_index], array[lower_index - 1]
			
			inplace_sort(start_index, lower_index - 1)
			inplace_sort(lower_index + 1, end_index)
	

	inplace_sort(0, len(array))
	return array






if __name__ == '__main__':
	test_array = list(set([randint(1, 10000) for _ in range(1000)]))

	print(f'Test Array: {test_array}')
	print(f'Array Length: {len(test_array)}')
