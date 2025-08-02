from problem2185 import Solution
import pytest


class TestSolution:
    @pytest.mark.parametrize(
        "words, pref, expected",
        [
            (["pay", "attention", "practice", "attend"], "at", 2),
            (["leetcode", "win", "loops", "success"], "code", 0),
        ],
    )
    def test_prefixCount(self, words, pref, expected):
        assert Solution.prefixCount("", words, pref) == expected
