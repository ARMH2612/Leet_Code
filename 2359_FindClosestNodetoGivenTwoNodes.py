def closestMeetingNode(edges, node1, node2):
    """
    :type edges: List[int]
    :type node1: int
    :type node2: int
    :rtype: int
    """
    val_node1 = edges[node1]
    val_node2 = edges[node2]
    dist1 = {}
    dist1[node1] = 0
    dist2 = {}
    dist2[node2] = 0
    distance = 0

    while val_node1 != -1:
        distance += 1
        if val_node1 in dist1.keys():
            break
        dist1[val_node1] = distance
        val_node1 = edges[val_node1]
    distance = 0
    while val_node2 != -1:
        distance += 1
        if val_node2 in dist2.keys():
            break
        dist2[val_node2] = distance
        val_node2 = edges[val_node2]

    keys1 = list(dist1.keys())
    keys2 = list(dist2.keys())

    keys3 = []
    # if len(keys1) > len(keys2):
    # for k in keys1:
    #     if k in keys2:
    #         keys3.append(k)
    # else:
    #     for k in keys2:
    #         if k in keys1:
    #             keys3.append(k)

    keys3 = list(set(keys1) & set(keys2))
    dist3 = {}
    for k in keys3:
        if dist1[k] > dist2[k]:
            dist3[k] = dist1[k]
        else:
            dist3[k] = dist2[k]

    dist3 = dict(sorted(dist3.items(), key=lambda item: item[1]))

    if len(dist3) > 0:
        val0 = dist3[list(dist3.keys())[0]]
        print('val 0 ', val0)
        dist4 = {}
        for k in dist3.keys():
            if dist3[k] == val0:
                dist4[k] = dist3[k]

        # print(dist4)
        if len(dist4) > 0:
            return sorted(dist4)[0]

    print(dist1)
    print(dist2)
    print(dist3)
    if len(keys3) >= 1:
        # print(keys3)
        # return keys3[0]
        return list(dist3.keys())[0]
    # elif len(keys3) == 1:
        # return max(dist1[keys3[0]], dist2[keys3[0]])
        # return keys3[0]
    else:
        return -1

# print(closestMeetingNode([4, 3, 0, 5, 3, -1], 4, 0))
# print(closestMeetingNode([4, 4, 4, 5, 1, 2, 2], 1, 1))
# print(closestMeetingNode([-1, 0], 1, 0))
# print(closestMeetingNode([5, 3, 1, 0, 2, 4, 5], 3, 2))
# 3:0     2:0     2
# 0:1     1:1     3
# 5:2     3:2     0
# 4:3     0:3     5
# 2:5     5:4     4
#         4:5

# print(closestMeetingNode([1, 2, -1], 0, 2))
# print(closestMeetingNode([2, 0, 0], 2, 0))
# 2:0     0:0
# 0:1     2:1

# 2
# 0


# print(closestMeetingNode([2, 0, 0], 2, 0))
# print(closestMeetingNode([4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6))
print(closestMeetingNode([5, 4, 5, 4, 3, 6, -1], 0, 1))
# print(closestMeetingNode([5, 3, 1, 0, 2, 4, 5], 3, 2))
# print(closestMeetingNode([1, 5, 5, 0, 6, 4, 0], 5, 0))
