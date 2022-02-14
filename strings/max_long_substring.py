
def longsubstring(s):
    
    if len(s) == 0:
        return 0
    
    subs = ""
    i = 0 
    j = 0
    a = []
    max_len = 0
    while(i < len(s)):
        if s[i] not in subs:
            subs += s[i]
            i += 1
            
        else:
            a = len(subs)
            if a > max_len:
                max_len = a
        
            subs = ""
            j += 1
            i = j

    return max_len

s = "ababababa"
print(longsubstring(s))