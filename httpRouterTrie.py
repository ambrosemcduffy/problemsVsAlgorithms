class Node:
    def __init__(self):
        self.children = {}
        self.pathComplete = False


class RouteTrie:
    def __init__(self,):
        self.root = None
        self._handler = "handler not found"
        self.pathComplete = False

    def insert(self, directory, _handler):
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
        node = self.root

        for name in path.split("/"):
            if name in node.children:
                node = node.children[name]
        return node


path_l = []


def findPath(node, path=""):
    if node.pathComplete:
        if node.children == {}:
            path_l.append(path)
            print(node._handler)

    for element, current_node in node.children.items():
        findPath(current_node, path+"/"+element)


myrouter = RouteTrie()
myrouter.insert("/root/file/path", "My root path")
myrouter.insert("/home/file/path", "My home file")

node = myrouter.find("/")
findPath(node, path="")
print(path_l)
