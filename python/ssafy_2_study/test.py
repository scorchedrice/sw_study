def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    right = [num for num in tail if num > pivot]
    left = [num for num in tail if num <= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


my_dict = {3: 'a', 2: 'b', 5: 'c'}
quick_sort(my_dict)