class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False # negative numbers are NOT palindrome
        div = 1
        while x/div>=10: # find maximum 100...0 such that x/div gives the first digit
            div *= 10
        while x: # while x>0
            if x/div!=x%10: return False # if first and last digits don't match, it's not a palindrome
            x = (x%div)/10 # after one cycle, chop off first and last digits
            div /= 100 # two digits chopped, div should be shortened by two 0's
        return True
