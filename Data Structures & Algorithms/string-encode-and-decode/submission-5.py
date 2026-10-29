class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(word)) + "#" + word for word in strs)
        

    def decode(self, s: str) -> List[str]:
        res = []

        
        index = 0

        while index < len(s):
            
            separetor = s.find("#", index)

            length = int(s[index: separetor])
            
            start = separetor + 1

            res.append(s[start: start + length])

            index = start + length
            
        return res