class Codec:
    def __init__(self):
        self.map = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.generateUniqueKey(6)
        self.map[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl]
        
    def generateKey(self, n):
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=n))
    
    def generateUniqueKey(self, n):
        key = self.generateKey(n)
        while key in self.map:
            key = self.generateKey(n)
        return key
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
