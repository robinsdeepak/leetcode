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
        self.integers = []
        self.index = 0
        q = [nestedList]
        
        # print(nestedList.isInteger())
        
        def dfs(el):
            if isinstance(el, list):
                for ch in el:
                    dfs(ch)
            else:
                if el.isInteger():
                    self.integers.append(el.getInteger())
                else:
                    for l in el.getList():
                        dfs(l)
        
        dfs(nestedList)
            
        
    
    def next(self) -> int:
        if self.hasNext():
            x = self.integers[self.index]
            self.index += 1
            return x
    
    def hasNext(self) -> bool:
         return self.index < len(self.integers)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())