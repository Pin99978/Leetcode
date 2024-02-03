#168ms O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        
        # ebats
        s = list(s)
        a = []
        for  i in s:
            
            a.append(i)
            if i == "*":

                a.pop()
                a.pop()
        return "".join(a)

            
