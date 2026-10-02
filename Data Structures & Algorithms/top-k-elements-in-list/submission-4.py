class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count = [[] for i in range(len(nums) + 1)]

        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        # frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        # res = [item for item in frequency]
        # return res[:k]

        for key, value in frequency.items():
            count[value].append(key)
        res = []
        for i in range(len(count) - 1, 0, -1):
            for item in count[i]:
                res.append(item)
                if len(res) == k:
                    return res
