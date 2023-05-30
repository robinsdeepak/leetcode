class MyHashSet:

    def __init__(self):
        self.n = 37
        self.data = [
            set() for _ in range(self.n)
        ]

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.data[idx].add(key)
        
    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.data[idx]:
            self.data[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.data[idx]
        
    def _hash(self, key):
        return key % self.n

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
