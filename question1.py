'''Given an array of integers return indices of the two numbers
that add up to a target number'''

# Given the index of two numbers that add up to the target
# each input has exactly one solution
# can't use same element twice

'''example array
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
# use a loop to go through the numbers.
# should be target - value = number to be found
# from there go through lists.
class Solution:
    ''' nums = Lists[int]
        target = int'''

    def twoSum(self, nums, target):
        previous_num = {} #adds previous number to new list to check if target = value that we are looking for
        for i, num in enumerate(nums):
            x = target - num
            if x not in previous_num:
                previous_num[num] = i
            else:
                return [previous_num[x], i]

