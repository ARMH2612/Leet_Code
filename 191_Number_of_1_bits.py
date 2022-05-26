class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        conv_n = str(n)
        sum = 0
        while n != 0:
            mask = n & (-n)
            n = n - mask
            sum += 1
        return sum
