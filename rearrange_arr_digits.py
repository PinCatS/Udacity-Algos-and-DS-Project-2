def partition(arr, left, right, pivot_index):
    pivot = arr[pivot_index]
    store_index = left

    # move pivot to the end
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]

    # move all elements smaller than or equal to pivot to the left
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # move the pivot to its final position
    arr[right], arr[store_index] = arr[store_index], arr[right]

    # find left boundary in case of pivot duplicates
    pivot_left_index = store_index
    while pivot_left_index >= 0 and arr[pivot_left_index] == pivot:
        pivot_left_index -= 1

    return (pivot_left_index + 1, store_index)


def bubble_sort(arr):
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1 - i:
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1


def select_pivot(arr, left, right):
    if (right - left) < 2:
        return left
    
    middle = left + (right - left) // 2
    arr2 = [(arr[left], left), (arr[middle], middle), (arr[right], right)]
    bubble_sort(arr2)
    return arr2[1][1]
    

def quicksort(arr, left, right):
    while left < right:
        #pivot_index = randint(left, right)
        pivot_index = select_pivot(arr, left, right)
        #pivot_index = left
        mid_left, mid_right = partition(arr, left, right, pivot_index)
        if (mid_left - left) < (right - mid_right):
            quicksort(arr, left, mid_left - 1)
            left = mid_right + 1
        else:
            quicksort(arr, mid_right + 1, right)
            right = mid_left - 1    


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quicksort(input_list, 0, len(input_list) - 1)
    first_number = 0
    second_number = 0
    for i in range(len(input_list)-1, -1, -1):
        if i % 2 == 0:
            first_number *= 10
            first_number += input_list[i]
        else:
            second_number *= 10
            second_number += input_list[i]
    return [first_number, second_number]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])