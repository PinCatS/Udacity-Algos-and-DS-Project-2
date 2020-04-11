# Autocomplete problem implementation description

Trie data structure is used for using the space efficiently.

**insert** operation takes O(n) time complexity, where n is the number of characters in the word that is added to the trie.

**find** operation takes O(n) time complexity, where n is a number of characters of the input prefix

**suffixes** operation takes O(n) time complexity, where n is a sum of suffixes length for the input node.

The **suffixes** operation uses recursion to traverse through each trie node under the input node and collects the suffixes into the list.

And finally **autocomplete** function utilizes **find** and **suffixes** to print all suffixes of the input prefix.
So the complexity is O(n).

