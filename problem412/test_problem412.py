from problem412 import Solution
import pytest

class TestSolution:

    @pytest.mark.parametrize("num, expected",[
        (3, ["1", "2", "Fizz"]),
        (5, ["1","2","Fizz","4","Buzz"]),
        (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
    ])

    def test_fizzBuzz(self, num, expected):
        assert Solution.fizzBuzz("", num) == expected