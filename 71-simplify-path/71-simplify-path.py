class Solution:
    def simplifyPath(self, path: str) -> str:
        splits = [x for x in path.split("/") if x != ""]
        temp = []
        for x in splits:
            if x == '..':
                if len(temp):
                    temp.pop()
            elif x != '.':
                temp.append(x)
        return ("/" if path[0] == "/" else "") + ("/".join(temp))
