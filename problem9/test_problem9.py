from problem9 import Solution
import pytest


class TestSolution:
  @pytest.mark.parametrize(
    "x, expected",
    [
      (121, True),
      (-121, False),
      (10, False),
    ],
  )
  def test_isPalindrome(self, x, expected):
    assert Solution.isPalindrome("", x) == expected
