from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(int(n/2)):
            temp = s[0 + i]
            s[0 + i] = s[n - 1 - i]
            s[n - 1 - i] = temp 
        return s      