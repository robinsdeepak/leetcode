class MyHashSet:

    def __init__(self):
        self.data = [[] for _ in range(100)]
    
    def getHash(self, key):
        return key % 100

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data[self.getHash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data[self.getHash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data[self.getHash(key)]
    
    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


