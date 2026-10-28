class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}

        for index, item in enumerate(nums):
            rest = target - item
            
            if rest in my_dict:

                rest_index = my_dict[rest]

                return [rest_index, index]
            else:
                my_dict[item] = index

        return []
