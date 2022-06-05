class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

class TextEditor:

    def __init__(self):
        self.root = Node("")
        self.cursor = self.root

    def addText(self, text: str) -> None:
        right = self.cursor.right
        if right:
            right.left = None
            
        node = None
        for char in text:
            node = Node(char)
            self.cursor.right = node
            node.left = self.cursor
            self.cursor = node
        
        if node and right:
            right.left = node
            node.right = right
        
    def deleteText(self, k: int) -> int:
        c = 0
        while c < k and self.cursor != self.root:
            tmp = self.cursor
            self.cursor = tmp.left
            self.cursor.right = tmp.right
            if tmp.right:
                tmp.right.left = self.cursor
            
            del tmp
            c += 1
        return c

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.cursor.left:
            self.cursor = self.cursor.left
            k -= 1
        
        return self.last_10_min()
        
    def cursorRight(self, k: int) -> str:
        while k > 0 and self.cursor.right:
            self.cursor = self.cursor.right
            k -= 1

        return self.last_10_min()
        
    
    def last_10_min(self):
        tmp = self.cursor
        text = ""
        c = 10
        while tmp != self.root and c > 0:
            text += tmp.char
            tmp = tmp.left
            c -= 1
        return text[::-1]
    
    def printText(self):
        tmp = self.root.right
        text = ""
        while tmp:
            text += tmp.char
            tmp = tmp.right
        print(text, self.cursor.char)

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)