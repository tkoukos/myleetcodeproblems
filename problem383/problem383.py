# class Solution:
#     def Ransom_Note(self, ransomNote: str, magazine:str) -> bool:
#         cntr_magazine = {}
#         for c in magazine:
#             if c in cntr_magazine:
#                 cntr_magazine[c] += 1
#             else:
#                 cntr_magazine[c] = 1

#         for c in ransomNote:
#             if c not in cntr_magazine or cntr_magazine[c] == 0:
#                 return False
#             else:
#                 cntr_magazine[c] -= 1

#         return True

from collections import Counter


class Solution:
    def Ransom_Note(self, ransomNote: str, magazine: str) -> bool:
        cntr_magazine = Counter(magazine)
        for c in ransomNote:
            if not cntr_magazine[c]:
                return False
            else:
                cntr_magazine[c] -= 1
        return True
