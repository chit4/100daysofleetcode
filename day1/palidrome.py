#https://leetcode.com/problems/palindrome-number/
#https://leetcode.com/submissions/detail/692070196/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return false
        number = x
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse