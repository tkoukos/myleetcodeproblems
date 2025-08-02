from problem344 import Solution
import pytest


class TestSolution:
    @pytest.mark.parametrize(
        "s, expected",
        [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
            (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        ],
    )
    def test_reverseString(self, s, expected):
        assert Solution.reverseString("", s) == expected
