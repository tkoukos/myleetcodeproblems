class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        n, p, j = len(words), 0, len(pref)
        for i in range(n):
            if words[i][0:j] == pref :
                p += 1
        return p