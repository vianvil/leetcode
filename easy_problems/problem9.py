class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        str_x = str(x)
        #converts the integer to string in order to use string slicing to reverse the order.
        if str_x[:] == str_x[::-1]:
            #[::-1] reverses the string, checks if it's equal to regular string, i.e. checking if palindrome
            return True
        else:
            return False