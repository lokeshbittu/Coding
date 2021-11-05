
def longsubstring(s):
    # if len(s) == 0 :
    #     return 0
    # else:
    #     start = 0
    #     end = 0
    #     stack = []
    #     main_stack = []
    #     for i in range(len(s)):
    #         if s[i] not in stack:
    #             print(s[i])
    #             stack.append(s[i])
    #             end += i
    #         main_stack.append(s[start:end+1])
    #         print(main_stack)
    #         if s[i] in stack:
    #             start = end
    #             end = start
    #     return len(max(main_stack, key=len))
    l=len(s)
    if l==0:
        return 0
    d={}
    for i in range(l):
        X=''    
        for j in range(i,l):
            if s[j] in X:
                d[X]=len(X)
                
                X=''
                break
            else:
                X=X+s[j]
        d[X]=len(X)
        print(d)
    return max(d.values())

s = "abcabcbb"
print(longsubstring(s))