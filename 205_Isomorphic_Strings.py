def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

            
    #  doesnt work always:
    # if len(s)!=len(t):
    #     return False
    
    # # fill the dictioanry:
    # dictioanry = {}
    # for i,c in enumerate(s):
    #     if dictioanry.get(c) == None:
    #         dictioanry[c] = t[i]
    # newWord = []
    # for c in t:
    #     try:
    #         key = list(dictioanry.keys())[list(dictioanry.values()).index(c)]
    #     except:
    #         key = False
    #     if key == False:
    #         newWord.append(c)
    #     else:
    #         newWord.append(key)

    # print(dictioanry)
    # print(''.join(newWord)==s)

# Always works:
    map_st = {}
    map_ts = {}
    for c1,c2 in zip(s,t):
        if(c1 not in map_st) and (c2 not in map_ts):
            map_st[c1] = c2
            map_ts[c2] = c1
        elif map_st.get(c1) != c2 or map_ts.get(c2)!=c1:
            return False;
    
    return True


s = "baa"
t = "cfa"
isIsomorphic(s, t)

    