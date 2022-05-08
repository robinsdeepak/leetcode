# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        
        for el in reversed(nestedList):
            self.stack.append(el)
    
    def makeTopInteger(self):
        while self.stack and not self.stack[-1].isInteger():
            ni = self.stack.pop(-1)
            for el in reversed(ni.getList()):
                self.stack.append(el)
        
    def next(self) -> int:
        self.makeTopInteger()
        
        el = self.stack.pop(-1)
        return el.getInteger()
        
    def hasNext(self) -> bool:
        self.makeTopInteger()
        return self.stack
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())