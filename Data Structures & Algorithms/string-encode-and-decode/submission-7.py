class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s))+ '#' + s for s in strs)

    def decode(self, s: str) -> List[str]:

        n = len(s)

        index = 0

        res = []

        while index < n:

            pos = s.find('#', index)

            length = int(s[index : pos])

            res.append(s[pos + 1 : pos + length  + 1])

            index = pos + length + 1
        
        return res

            

