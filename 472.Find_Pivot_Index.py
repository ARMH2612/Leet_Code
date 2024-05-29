def pivotIndex(nums):
    # p_index = -1
    n = len(nums)
    for i in range(n):
        print(nums[0:i], sum(set(nums[0:i])))
        print(nums[i:n], sum(set(nums[i:n])))
        print("--------------------------")
        somme = sum(set(nums[0:i]))
        for j in range(i, n):
            if somme == sum(set(nums[j:n])):
                return i
    return -1


# print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
# print(pivotIndex([2, 1, -1]))
