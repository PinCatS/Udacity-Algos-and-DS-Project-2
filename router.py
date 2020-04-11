from collections import defaultdict

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if len(path) == 1 and path[0] == '':
            return

        node = self.root
        for p in path:
            node = node.children[p]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(path) == 1 and path[0] == '':
            return self.root.handler

        node = self.root
        for p in path:
            if p not in node.children:
                return None
            node = node.children[p]
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)

    def insert(self):
        # Insert the node as before
        pass

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.router_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.router_trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.router_trie.find(self.split_path(path))
        if handler is None:
            return self.not_found_handler
        return handler


    def split_path(self, path):
        path_parts = path.split('/')
        
        # remove last '' path part to handle the case when
        # there is a trailing slash
        # e.g. /about and /about/
        if len(path_parts) > 1 and path_parts[-1] == '':
            path_parts.pop()
        return path_parts

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a router

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one