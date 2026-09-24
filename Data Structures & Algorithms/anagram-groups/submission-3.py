class Solution:

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     for item in s:
    #         if item not in t:
    #             return False
    #         if s.count(item) != t.count(item):
    #             return False 
    #     return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            hash_value = [0] * 26
            for c in s:
                hash_value[ord(c) - ord("a")] += 1
            result[tuple(hash_value)].append(s)

        return list(result.values())

            