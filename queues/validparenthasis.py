
def validity(s):
    stack = []
    obrac = ["(","[","{"]
    cbrac = [")","]","}"]
    i = 0
    while(i < len(s)):
        if s[i] in obrac:
            stack.append(s[i])      
            print(stack)
        if s[i] in cbrac:
            stack.pop()      
            print(stack)
        i += 1
    
    if stack:
        return False
    else:
        return True

s = "{[]}"
print(validity(s))