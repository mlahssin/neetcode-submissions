class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = []
        for item in nums:
            if item in checked:
                return True
            checked.append(item)
        return False

        