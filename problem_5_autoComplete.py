class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):

        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.isWord = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node

    def getSuffix(self, prefix=""):
        if prefix is None:
            return None

        prefix_node = self.find(prefix)
        if not prefix_node:
            return -1
        suffix_list = []

        def findSuffix(prefix_node, suffix=""):
            if prefix_node.children == {}:
                suffix_list.append(suffix)

            if prefix_node.isWord and suffix not in suffix_list and suffix != "":
                suffix_list.append(suffix)

            for char, suffix_node in prefix_node.children.items():
                findSuffix(suffix_node, suffix+char)

        findSuffix(prefix_node)
        return suffix_list


trie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym", "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"]

for word in wordList:
    trie.add(word)


# Edge cases
prefix = "tri"
suffix = trie.getSuffix(prefix)
print(suffix)

prefix = "ant"
suffix = trie.getSuffix(prefix)
print(suffix)

prefix = "fu"
suffix = trie.getSuffix(prefix)
print(suffix)


# Test cases

# Returns -1
print(trie.getSuffix("cat"))

# Returns None
print(trie.getSuffix(None))
