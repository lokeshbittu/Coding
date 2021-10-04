

# sym = {"I":1, "V":5,"X":10, "L":50,"C":100,"D":500, "M":1000}

def romanToInt(s):
    sym = {"I":1, "V":5,"X":10, "L":50,"C":100,"D":500, "M":1000}
    count = 0
        
    for i in range(len(s)):
        if i == 0:
            count += sym[s[i]]
            print(count)
        if sym[s[i-1]] >= sym[s[i]] and i > 0:
            count += sym[s[i]]
            print(count)
        elif sym[s[i-1]] < sym[s[i]]:
            count += sym[s[i]] - sym[s[i-1]]
            print(count)
    return count

print(romanToInt("LVIII"))