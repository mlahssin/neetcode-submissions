class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hash_map = {}

        if not s:
            return 0

        
        n = len(s)

        right = 0
        res = 0
        left = 0
        while right < n:
            
            if s[right] not in hash_map:
                hash_map[s[right]] = 1
            else:
                hash_map[s[right]] += 1
    
            key_f, occ = max(hash_map.items(), key=lambda x: x[1])
                
            while left <= right and right - left + 1 - occ > k:
                
                hash_map[s[left]] -= 1
                left += 1
                occ = max(hash_map.values())
            
            res = max(res, right - left + 1)

            right += 1

        return res     


print(Solution().characterReplacement("ABAA", 0))


# s="ABAA"
# k=0