class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + '#' + s for s in strs)

    def decode(self, s: str) -> List[str]:

        res = []

        index = 0
        n = len(s)
        while index < n:
            pos = s.find('#', index)

            lenght = int(s[index :pos])


            res.append(s[pos + 1: pos + 1 + lenght])
            
            index = pos + 1 + lenght
        return res

