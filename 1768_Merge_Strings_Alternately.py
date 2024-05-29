def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    merged = ''
    for (c1,c2) in zip(word1,word2):
        merged+=f"{c1}{c2}"
    
    if(len(word1) > len(word2)):
         merged+=''.join(word1[int(len(merged)/2):])
    elif len(word1) < len(word2):
         merged+=''.join(word2[int(len(merged)/2):])
    
    print(merged)

mergeAlternately('ab', 'pqrs')