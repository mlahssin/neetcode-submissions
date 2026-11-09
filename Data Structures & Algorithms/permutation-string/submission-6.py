class Solution:

    def alpha_map_finder(self,s):
        alpha_map = [0] * 26

        for c in s:
            alpha_map[ord(c) - ord('a')] += 1

        return alpha_map


    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        if len(s1) > len(s2) or len(s1) == 0:
            return False

        s1_map = self.alpha_map_finder(s1)

        # for c in s1:
        #     alpha_map[ord(c) - ord('a')] += 1
        
        left = 0
        right = len(s1)



        while left + right - 1< len(s2):
            s2_map = self.alpha_map_finder(s2[left: left + right])

            if s2_map == s1_map:
                return True
            left += 1
        return False

