def QuickSort(myList):
    if len(myList) < 2:
        return myList
    
    left, equal, right = [], [], []
    pivot = myList[0]

    for element in myList:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    return QuickSort(left) + equal + QuickSort(right)




if __name__ == '__main__':
    random_array = [randint(0, 100) for _ in range(1000)]
    print(random_array)
    print(QuickSort(random_array))
