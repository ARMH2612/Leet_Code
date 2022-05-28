class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum = 0
        # sum2 = 0
        # i = 1
        # for number in nums:
        #     sum = sum + number
        #     sum2 = sum2 + 1 * i
        #     i = i+1

        # return sum2 - sum
        n = len(nums)
        suit = n*(n+1)//2
        sum_nums = sum(nums)
        return suit - sum_nums
