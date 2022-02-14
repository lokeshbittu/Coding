

def google(s):
    
    max_length = 0
    result = s[0]
    for i in range(len(s)):
        for j in range(len(s)-1,i, -1):
            if s[i] == s[j]:
                if (max_length < j-i+1):
                    max_length = j-i+1
                    result = s[i:j+1]

    return result


s = "cbaabaab"
print(google(s))