# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         max_s = 0
#         for wealth in accounts:
#             s = 0
#             for i in range(len(wealth)):
#                 s += wealth[i]
#             if s > max_s:
#                 max_s = s
#         return max_s


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_s = 0
        for wealth in accounts:
            max_s = max(max_s, sum(wealth))
        return max_s
