def gcdOfStrings(str1: str, str2: str) -> str:
        if(len(str1)>len(str2)):
            return GCDS(str1, str2) or ""
        else:
            return GCDS(str2, str1) or ""
            
                    

def GCDS(str1, str2):
    gcds_array = [None]
    for i in range(1,len(str2)+1):
        if len(str2) % len(str2[:i]) == 0:
            gcds = str2[:i] * int(len(str2)/i)
            if gcds == str2:
                if(str1 == (str2[:i] * int(len(str1)/i))):
                    gcds_array.append(str2[:i])
    
    return gcds_array[-1]
print(gcdOfStrings( 'LEET', 'CODE' ))