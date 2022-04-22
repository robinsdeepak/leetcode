class MyHashMap:

    def __init__(self):
        self.data = [ [] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        idx = self.getIndex(key)
        hash_ = self.getHash(key)
        
        if idx != -1:
            self.data[hash_][idx][1] = value
        else:
            self.data[hash_].append([key, value])
        
    def get(self, key: int) -> int:
        idx = self.getIndex(key)
        hash_ = self.getHash(key)

        if idx != -1:
            return self.data[hash_][idx][1]
        return -1

    def remove(self, key: int) -> None:
        idx = self.getIndex(key)
        hash_ = self.getHash(key)
        if idx != -1:
            self.data[hash_].pop(idx)

    def getIndex(self, key):
        for i, el in enumerate(self.data[self.getHash(key)]):
            if key == el[0]:
                return i
        return -1
    
    def getHash(self, key):
        return key % 1000

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)x