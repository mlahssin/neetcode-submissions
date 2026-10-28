

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        len_s = len(s)
        len_t = len(t)

        if len_s !=  len_t:
            return False


        hash_s = [0] * 26

        for c in s:
            index = ord(c) - ord('a')
            hash_s[index] += 1


        hash_t = [0] * 26

        for c in t:
            index = ord(c) - ord('a')
            hash_t[index] += 1
        return hash_s == hash_t
        
        
        

            

        for item in s:

            if item not in hash_set_s:
                hash_set_s[item] = 1
            else:
                hash_set_s[item] += 1
        
        hash_set_t = {}

        for item in t:
            if item not in hash_set_t:
                hash_set_t[item] = 1
            else:
                hash_set_t[item] += 1
        

        return hash_set_s == hash_set_t
        