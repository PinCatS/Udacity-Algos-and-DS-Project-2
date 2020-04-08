# Rearrange array digits implementation description

I have implemented quciksort algorithm to sort the array.
After sorting, it is enough to run from the end to the begining of the array to build two digits that give the maximum sum.

Runtime complexity of the algorithm is O(nlogn) and
space complexity is O(logn) where n in both cases is a number of input elements.

Run through the sorted array takes Theta(n) + sorting algorithm takes O(nlogn) in average.

Quciksort algorithm on avarage will have O(nlogn) time complexity and O(logn) space complexity in a worse case since recursion was used. N in both cases is a number of elements in the array.

There were several optimisations used in a quicksort.

The pivot is choosen by taking first elemnt, middle and end elements and their median is used as a pivot. (to sort three elements, I use bubble sort. In this case it can be treated as O(1)). Such approach is used in the Intro sort and in most cases the pivot will be choosen good enough to have balanced partition.

Sometime pivot can be choosen using random function but in this case it is bad for debugging. So Intro sort way is more preferred.

Another optimization is related to partitioning. Instead of return the index of the final position of the pivot element, I return two indecies in case there are duplicates - left and the right boundaries. It prevents performance degradation in case if there are many duplicates in the array.

The last optimization is made for guarantee O(logn) time complexity in worse case, not in average.
In quicksort there is a tailrecursion, so we can eliminate one of the recursive calls and it even doesn't matter against what side each time recursion is called. So depending on the sizes of left and right siedes, recursion is called against the smaller one.