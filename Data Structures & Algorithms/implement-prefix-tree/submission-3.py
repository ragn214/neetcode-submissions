class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

#My slow version
    # class PrefixTree:

    #     def __init__(self):
    #         self.words = []

    #     def insert(self, word: str) -> None:
    #         self.words.append(word)

    #     def search(self, word: str) -> bool:
    #         return word in self.words

    #     def startsWith(self, prefix: str) -> bool:
    #         for i in self.words:
    #             if prefix == i[:len(prefix)]:
    #                 return True
    #         return False