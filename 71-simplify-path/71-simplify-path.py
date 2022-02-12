class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = []
        for x in path.split("/"):
            if x == '..':
                if len(temp):
                    temp.pop()
            elif x != '.' and x != "":
                temp.append(x)
    
        return  "/"+ "/".join(temp)
