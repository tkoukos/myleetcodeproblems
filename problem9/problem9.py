class Solution:
  def isPalindrome(self, x: int) -> bool:
    reverse = 0
    s = x
    while x > 0:
      temp = x % 10
      reverse = (reverse * 10) + temp
      x //= 10
    if reverse == s:
      return True
    else:
      return False
