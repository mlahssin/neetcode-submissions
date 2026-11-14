# from typing import List
# from collections import deque
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

#         if len(position)!= len(speed):
#             return 0
        

#         n = len(position)

#         index = 0
#         pos_spe = {}

#         while index < n:

#             pos_spe[position[index]] = speed[index]

#             index += 1
        

#         # pos_spe = dict(sorted(pos_spe.items(), key=lambda x:x[0], reverse=True))
#         pos_spe = dict(sorted(pos_spe.items(), key=lambda x:x[0], reverse=True))

#         times = deque()

#         for pos, sp in pos_spe.items():
#             arrive = (target - pos) / sp
#             if not times:
#                 times.append(arrive)
#             else:
#                 if times[-1] < arrive:
#                     times.append(arrive)

#         # print(pos_spe)
#         return len(times)


# print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

from typing import List
from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position)!= len(speed):
            return 0
        

        n = len(position)

        index = 0
        pos_spe = {}

        while index < n:

            pos_spe[position[index]] = speed[index]

            index += 1
        

        # pos_spe = dict(sorted(pos_spe.items(), key=lambda x:x[0], reverse=True))
        pos_spe = dict(sorted(pos_spe.items(), key=lambda x:x[0]))

        times = deque()

        for pos, sp in pos_spe.items():
            arrive = (target - pos) / sp
            if not times:
                times.append(arrive)
            else:
                if times[-1] > arrive:
                    times.append(arrive)
                else:
                    while times and  times[-1] <= arrive:
                        times.pop()
                    times.append(arrive)

        # print(pos_spe)
        return len(times)


print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))


            
        
            
        