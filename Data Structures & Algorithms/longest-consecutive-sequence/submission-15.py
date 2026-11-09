class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        longest = 0

        for n in nums:

            lenght = 0
            if n - 1 not in numSet:
                while n + lenght in numSet:
                    lenght += 1

            longest = max(longest, lenght)

        return longest