class TriNode:
    def __init__(self):
        self.children = [None] * 26
        self.childCount = 0
        self.isLeaf = False

class Solution(object):
    def insert(self,root,s):
        pCrawl = root
        for c in s:
            index = ord(c) - ord('a')
            if (pCrawl.children[index] is None):
                pCrawl.children[index] = TriNode()
                pCrawl.childCount += 1
            pCrawl = pCrawl.children[index]
        pCrawl.isLeaf = True

    def traverseTrie(self,root,s):
        pCrawl = root
        i = 0

        while pCrawl.childCount == 1 and not pCrawl.isLeaf:
            index = ord(s[i]) - ord('a')
            i += 1
            pCrawl = pCrawl.children[index]
        return s[:i]

    def longestCommonPrefix(self,strs):
        root = TriNode()

        for string in strs:
            self.insert(root,string)
        
        return self.traverseTrie(root,strs[0])
        """
        :type strs: List[str]
        :rtype: str
        """
        