# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        enc = ""
        q1 = [root]
        
        while (len(q1)):
            q2 = []
            for node in q1:
                if node is None:
                    enc += "N "
                    continue
                enc += str(node.val) + " "
                q2.append(node.left)
                q2.append(node.right)
            q1 = q2
        return enc
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        
        if nodes[0] == "N":
            return None
        
        root = TreeNode(int(nodes[0]))
        q1 = [root]
        
        index = 1
        
        while index < len(nodes):
            q2 = []
            for node in q1:
                left = TreeNode(int(nodes[index])) if nodes[index] != "N" else None
                index += 1
                if (index >= len(nodes)):
                    break
                right = TreeNode(int(nodes[index])) if nodes[index] != "N" else None
                index += 1
                
                node.left = left
                node.right = right
                
                if left:
                    q2.append(left)
                if right:
                    q2.append(right)
            q1 = q2
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))