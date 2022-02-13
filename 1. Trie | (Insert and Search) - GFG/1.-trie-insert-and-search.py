#User function Template for python3


#Function to insert string into TRIE.
def insert(root,key):
    ptr = root
    for char in key:
        idx = ord(char) - 97
        if not ptr.children[idx]:
            ptr.children[idx] = TrieNode()
        ptr = ptr.children[idx]
    ptr.isEndOfWord = True

#Function to use TRIE data structure and search the given string.
def search(root, key):
    ptr = root
    for char in key:
        idx = ord(char) - 97
        if not ptr.children[idx]:
            return False
        ptr = ptr.children[idx]
    return ptr.isEndOfWord

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        if search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends