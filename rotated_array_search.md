# Rotated array search implementation description
There is still binary search algorithm is used but slightly modified to handle the shift.

So the time complexity is O(logn), where n is a number of elements to search.
The space complexity is O(1) because we don't need any additional data structures and the implementation is not via recursion.

The modification to handle the shift is based on the fact that if middle element is greater than the start element, the left side doesn't contain the pivot, so we could safely do the check if the traget is lying between start and middle, otherwise right side doesn't have the pivot, so we can safely check if the target is lying betweem middle and the end.