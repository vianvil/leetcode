class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
             #Iterate through the list and gets index of array(nums) which is set to i

            if nums[i]+nums[i+1] == target:
             #Checks if the sum of nums at index i and i+1 is equal to target
             return (i, i+1)
            #returns the index at which the sum is equal to target