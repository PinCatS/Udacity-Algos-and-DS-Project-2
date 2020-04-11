def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       arr(list): List to be sorted
    """
    zero_index = 0
    current_index = 0
    two_index = len(arr) - 1
    while current_index < len(arr) and current_index <= two_index:
        if arr[current_index] == 0:
            arr[current_index] = arr[zero_index]
            arr[zero_index] = 0
            zero_index += 1
            current_index += 1
        elif arr[current_index] == 2:
            arr[current_index] = arr[two_index]
            arr[two_index] = 2
            two_index -= 1
        else:
            current_index += 1
    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])