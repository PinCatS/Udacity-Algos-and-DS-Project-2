# Router implementation description
Router is implemented using Trie data structure.

**add_handler** and **lookup** functions takes O(n) time complexity, where n is a number of path parts. We also need to take into account that both of these functions uses **split_path** function that takes O(n) time complexity where n is a number of characters in the path.

To handle the traling slash (e.g. '/home' and '/home/') it is enough to pop the last element from the list of path parts in case we have the trailing slash because in this case we will get '' element as the last emenet of the list (e.g. ['', home, ''])
