class Codec:
    def __init__(self):
        self.map = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.generateKey(6)
        self.map[key] = longUrl
        return 'http://tinyurl.com/' + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split('/')[-1]
        return self.map[key]
        
    def generateKey(self, n):
        key = "".join(random.choices(string.ascii_lowercase + string.digits, k=n))
        while key in self.map:
            key = "".join(random.choices(string.ascii_lowercase + string.digits, n))
        
        return key
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
