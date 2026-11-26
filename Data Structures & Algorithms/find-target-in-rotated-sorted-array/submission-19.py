# # class Solution:
# #     def search(self, nums: List[int], target: int) -> int:

# #         l = 0

# #         r = len(nums) - 1

# #         while l <= r:
# #             first = nums[l]

# #             middle = (l + r) // 2

# #             if nums[middle] == target:
# #                 return middle

# #             if nums[l] <= nums[middle]:
# #                 if target < first < nums[middle]:

# #                     l = middle + 1
# #                 else:

# #                     r = middle - 1
# #             else:

# #                 if nums[middle] < target:
# #                     l = middle + 1
# #                 else:
# #                     r = middle - 1
            
# #         return -1






# class Solution:
#     def search(self, nums: List[int], target: int) -> int:


#         l, r = 0 , len(nums) - 1


#         while l <= r:

#             m = (l + r) // 2


#             if nums[m] == target:
#                 return m
            
#             if nums[l] > nums[m]:

#                 if target < nums[m] <= nums[r]:

#                     l = m + 1
#                 else:
#                     r = m - 1
            
#             else:

#                 if nums[m] > target:
                    
#                     r = m - 1
#                 else:

#                     l = m + 1
            
        
#         return -1








class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2 

            if nums[m] == target:
                return m
            

            # left sorted array

            if nums[l] <= nums[m]:

                if target > nums[m] or target < nums[l]:

                    l = m + 1
                else:

                    r = m - 1
                
            else:

                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1


        return -1


                # right sorted array




            


            


































