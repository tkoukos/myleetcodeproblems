from problem1342 import Solution
import pytest


class TestSolution:
    @pytest.mark.parametrize("num, expected", [(14, 6), (8, 4), (123, 12)])
    def test_numberOfSteps(self, num, expected):
        assert Solution.numberOfSteps("", num) == expected
