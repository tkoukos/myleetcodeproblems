# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         for i in range(1,n):
#             nums[i] = nums[i] + nums[i - 1]
#         return nums

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        g = []
        current_sum = 0
        for num in nums:
            current_sum += num
            g.append(current_sum)
        return g