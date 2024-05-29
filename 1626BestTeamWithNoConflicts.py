
def bestTeamScore(scores, ages):
    # prev_age = 0
    # prev_score = 0
    # somme = 0
    # sommes = []
    # i = 0
    # while i < len(ages):
    #     if (ages[i] < prev_age and scores[i] > prev_score) or (prev_age < ages[i] and prev_score > scores[i]):
    #         sommes.append(somme)
    #         print("somme init", scores[i])
    #         somme = scores[i]
    #     else:
    #         # if prev_score < scores[i]:
    #         print(somme, scores[i], end=' ')
    #         somme += scores[i]
    #         print(somme)

    #     prev_age = ages[i]
    #     prev_score = scores[i]
    #     i += 1
    # sommes.append(somme)
    # print(sommes)
    # return max(sommes)
    dic = {}

    for i in range(len(ages)):
        if ages[i] in dic.keys():
            dic[ages[i]].append(scores[i])
        else:
            dic[ages[i]] = [scores[i]]

    dic = dict(sorted(dic.items()))
    for k in dic.keys():
        dic[k] = sorted(dic[k])
    # print(dic)
    sommes = []

    while len(dic) > 0:
        key = 0
        p = 0
        for k in dic.keys():
            if p == 0:
                key = k
                max_val = dic[k][len(dic[k])-1]
                somme = sum(dic[k])
            else:
                vals = dic[k]
                for v in vals:
                    if v >= max_val:
                        somme += v

                if vals[len(vals)-1] > max_val:
                    max_val = vals[len(vals)-1]

            p += 1
        sommes.append(somme)
        del dic[key]
    return max(sommes)


print(bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]))
print(bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]))
print(bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]))
print(bestTeamScore([9, 2, 8, 8, 2], [4, 1, 3, 3, 5]))
print(bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]))
