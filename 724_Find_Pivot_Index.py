
def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # // my solution, takes lotta run time
    # for i in range(len(nums)):
    #     if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
    #         return i
    # return -1

    # // leetCode solution:
    S = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (S-leftsum - x):
            return i
        leftsum += x
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
