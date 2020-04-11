def partition(arr, left, right, pivot_index):
    """
    Partition the array into three groups: less that pivot, equal to it and more than pivot

    Args:
       input_list(list): Input List
       left(int): start index
       right(int): end index
       pivot_index(int): index of the pivot element

    Returns:
       (int),(int): left and right index - boundary of the pivot element on the right place
       when array is sorted. All elements to the left index are smaller than the pivot,
       all element to the right inidex are bigger. All elements between left and right (including them)
       are equla to the pivot.
    """
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
    """
    Bubble sort

    Args:
       input_list(list): Input List
    Returns:
       Sorting happens in place, thus origina array is modified, nothing is returned
    """
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1 - i:
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1


def select_pivot(arr, left, right):
    """
    Selects the pivot element by choosing the first, last and the middle
    element from the array and returns the index of their median
    Used by the quicksort functions.

    bubble sort is used to sort the arrau of three. Because it sorts only three
    elemnts, the time complexity can be considered as O(1)

    Args:
        arr(list): input_list array
        left(int): start index of a subarray
        right(int): end index of a subarray
    Returns:
       (int): index of median of three elements(first, last, middle)
    """
    if (right - left) < 2:
        return left
    
    middle = left + (right - left) // 2
    arr2 = [(arr[left], left), (arr[middle], middle), (arr[right], right)]
    bubble_sort(arr2)
    return arr2[1][1]

    
def quicksort(arr, left, right):
    """
    Sort elements in ascending order. Intro sorting implementation of quicksort

    Uses median of left, right and middle element of th array as a pivot

    Recursion is used. Depending on the size of the left and right subarray I select
    against what I need to call recursion.
    It guarantees O(logn) space complexity in the worst case instead of the average.

    Partition returns two indexes instead of one
    to prevent degradation of efficiency in case of many duplicates.

    Args:
       arr(list): list of elements to sort
       left(int): star index of the array/subarray
       right(int): end index of the array/subarray
    Returns:
       array is sorted in place, so nothing is returned
    """
    while left < right:
        pivot_index = select_pivot(arr, left, right)
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


# Helper function for testing
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 0, 0, 0], [0, 0]])
test_function([[], [0, 0]])