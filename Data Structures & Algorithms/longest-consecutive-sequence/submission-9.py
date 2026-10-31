import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash_set = set()

        # if not nums:
        #     return 0

        # for n in nums:
        #     hash_set.add(n)

        # heap = []

        # for item in hash_set:
        #     heapq.heappush(heap, item)

        # n = len(hash_set)

        # counts = [1] * n

        # index = 0

        # elt = heapq.heappop(heap)

        # while heap:
        #     item = heapq.heappop(heap)

        #     if item == elt + 1:
        #         counts[index] += 1
        #         elt = item
        #     else:
        #         elt = item
        #         index += 1
        
        # return max(counts)

        numSet = set(nums)
        longest = 0

        for n in nums:

            if n - 1 not in numSet:
                # start of a new_sequence
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest 


            


        

        