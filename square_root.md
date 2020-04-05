# Square root of integer implementation
The implementation uses binary search algorithm idea to find the floor of the square root of the integer - the number square of which equals to the input number or closest smaller to it.

Thus, it takes O(logn) of time complexity, where n is the input integer square root of which we need to find. That is because on every iteration we halve the search region.

There is a further optimization. We only need to search through n/2 numbers instead of n numbers.

The space complexity is O(1) since we don't use any additional data structures or recursion.