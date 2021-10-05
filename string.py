
from collections import Counter

def wordbreak(s, wordDict):
    # worddict = ""
    # s1 = Counter(s)
    # print(s1)
    # for i in wordDict:
    #     worddict += i
    
    # wrd = Counter(worddict)
    
    # s1_count = 0
    # wrd_count = 0
    # for key in s1:
    #     s1_count += s1[key]
    
    # for key in wrd:
    #     wrd_count += wrd[key]
        
    # if s1_count >= wrd_count:
    #     return True
    # else:
    #     return False
    dp = [False for i in range(len(s))]
    print(dp)

String = "leetcode"
wordDict = ["leet","code"]
wordbreak(String, wordDict)