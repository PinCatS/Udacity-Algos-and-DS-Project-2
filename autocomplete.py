from collections import defaultdict

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.word_end = False
        self.children = defaultdict(TrieNode)

    def suffixes(self, suffix = '', s = []):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        for c in self.children:
            self.children[c].suffixes(suffix + c)

        if self.word_end and suffix is not '':
            s.append(suffix)
        
        return s

    def __str__(self):
        return f'Node({self.children.keys()}, {self.word_end})'
            

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word_end = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def is_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word_end


def autocomplete(prefix):
    if prefix != '' and prefix is not None:
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

autocomplete('fun')
print('-'*10)
autocomplete('')
print('-'*10)
autocomplete(None)
print('-'*10)
autocomplete('ar')
print('-'*10)
autocomplete('a')



