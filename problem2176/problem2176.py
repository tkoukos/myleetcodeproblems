from typing import List

# class Solution:
#     def countPairs(self, nums: list[int], k: int) -> int:
#         n = len(nums)
#         p = 0
#         for i in range(n):
#             for j in range(n):
#                 if nums[i] == nums[n - 1 - j] and i < (n - 1 - j):
#                     m = i*(n - 1 - j)
#                     if m%k == 0:
#                         p += 1
#         return p


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n, p = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i < j and (i * j) % k == 0:
                    p += 1
        return p
