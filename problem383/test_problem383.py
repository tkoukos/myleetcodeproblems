from problem383 import Solution
import pytest

class TestSolution:

    @pytest.mark.parametrize("ransomNote, magazine, expected", [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True)
    ])

    def test_Ransom_Note(self, ransomNote, magazine, expected):
        assert Solution.Ransom_Note("", ransomNote, magazine) == expected