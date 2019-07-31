def value(k): 
    if (k == 'I'): 
        return 1
    if (k == 'V'): 
        return 5
    if (k == 'X'): 
        return 10
    if (k == 'L'): 
        return 50
    if (k == 'C'): 
        return 100
    if (k == 'D'): 
        return 500
    if (k == 'M'): 
        return 1000
    return -1
def RD(s): 
    res = 0
    i = 0
    while (i < len(s)): 

        s1 = value(s[i]) 
  
        if (i+1 < len(s)): 

            s2 = value(s[i+1]) 
            if (s1 >= s2): 
                res = res + s1 
                i = i + 1
            else: 
                res = res + s2 - s1 
                i = i + 2
        else: 
            res = res + s1 
            i = i + 1
    print(res)  
ni=input()
RD(str(ni))
