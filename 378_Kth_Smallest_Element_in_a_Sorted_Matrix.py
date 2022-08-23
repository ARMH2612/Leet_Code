def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    mat = []
    mat += [n for m in matrix for n in m]
    print(sorted(mat)[k-1])


kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
