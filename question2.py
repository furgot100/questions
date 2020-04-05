'''Given an integer Reverse the digits of it'''
'''Assume the enviorment can only store 32-bit signed integers.
should return 0 if it goes past'''

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0: #For positive numbers
            rev = int(str(x)[::-1])
        if x <= 0: # For negative numbers
            rev =-1 * int(str(x * -1)[::-1])
        min = -2 ** 31
        max = 2 ** 31 -1
        if rev not in range(min, max): # checks if number is between range
            return 0
        else:
            return rev