class Node:
    """ Node for holding data to be implemented with trie"""
    def __init__(self):
        self.children = {}
        self.pathComplete = False
        self._handler = "not found handler"


class RouteTrie:
    """ Router Trie for implementing our router"""
    def __init__(self):
        self.root = None

    def insert(self, directory, _handler):
        """ inserts a file directory into our trie
        Args:
            directory (str): string path
            _handlder (str): string handle
        """
        if self.root is None:
            self.root = Node()

        node = self.root
        for path in directory.split("/"):
            if path not in node.children:
                node.children[path] = Node()
            node = node.children[path]
        
        node.pathComplete = True
        node._handler = _handler

    def find(self, path):
        """Finds node associated with path
        Args:
            path (str): string path
        Returns:
            (class): node class with handler and trie data
        """
        node = self.root
        
        for name in path.split("/"):
            if name in node.children:
                node = node.children[name]
            else:
                return None
        return node



class Router(object):
    """ Router Class"""
    def __init__(self):
        self.myTrie = RouteTrie()
    
    def lookup(self, path):
        """ looks path handler based on path
        Args:
            path (str): string path
        Returns (str): path handler
        """
        
        if path == "/":
            return "root handler"
        
        # if last element in path is "/" remove it
        if path[-1] == "/":
            path = path[:-1]

        node = self.myTrie.find(path)
        
        def recursiveSearch(node, path=""):
            """ Recursive Search for path handler
            Args:
                node (class): trie node class
                path (str): string path
            Returns:
                (str): string handler
            """
            
            if node is not None:
                if node._handler:
                    return node._handler
            
                for element, current_node in node.children.items():
                    if element != '':
                        return recursiveSearch(current_node, path + "/" + element)
                    else:
                        return -1
        
        handler = recursiveSearch(node)
        
        if handler is None:
            return "not found handler"
        else:
            return handler
    
    def addHandler(self, path, handler):
        """ inserts handler into trie node
        Args:
            path (str): string path
            handler (str): string handler to path
        """
        self.myTrie.insert(path, handler)


router = Router()
router.addHandler("/home/about", "about handler")

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' 
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
