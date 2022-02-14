def generateParenthesis(n):
    ans = []
    def backtrack(S = [], left = 0, right = 0):
        if len(S) == 2 * n:
            print(S)
            ans.append("".join(S))
            return
        if left < n:
            print("left")
            S.append("(")
            
            backtrack(S, left+1, right)
            
            S.pop()
        if right < left:
            print("right")
            S.append(")")
            
            backtrack(S, left, right+1)
            S.pop()
    backtrack()
    return ans

print(generateParenthesis(3))





