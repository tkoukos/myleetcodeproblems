from problem2176 import Solution
import pytest


class TestSolution:
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([3, 1, 2, 2, 2, 1, 3], 2, 4),
            ([1, 2, 3, 4], 1, 0),
        ],
    )
    def test_countPairs(self, nums, k, expected):
        assert Solution.countPairs("", nums, k) == expected
