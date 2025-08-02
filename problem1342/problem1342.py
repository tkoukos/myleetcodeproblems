class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        for i in range(1, num + 1):
            if num % 2 == 0:
                num = num // 2
                if num == 0:
                    break
                step += 1
            else:
                num = num - 1
                step += 1
        return step
