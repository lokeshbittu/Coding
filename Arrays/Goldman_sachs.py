def countAnalogousArrays(arr , lowerBound , upperBound):
    
    # maxdiff = float('-inf')
    # mindiff = float('inf')
    # runningsum = 0
    # if len(consecutiveDifference) == 0:
    #     return 0

    # if upperBound < lowerBound :
    #     return 0

    # for diff in consecutiveDifference:
    #     runningsum+=diff
    #     print(runningsum)

    #     if runningsum > maxdiff:
    #         maxdiff = runningsum

    #     if runningsum < mindiff:
    #         mindiff = runningsum

    # maxvalidupperbound = upperBound + mindiff if upperBound+mindiff < upperBound else upperBound
    # print("maxvalidupperbound:",maxvalidupperbound)
    # minvalidlowerbound = lowerBound + maxdiff if lowerBound + maxdiff > lowerBound else lowerBound
    # print("minvalidlowerbound:",minvalidlowerbound)
    
    # if maxvalidupperbound >= minvalidlowerbound:
    #     return maxvalidupperbound - minvalidlowerbound + 1
    # else:
    #     return 0
# ----------------------
    start = lowerBound
    total = 0
    low = lowerBound
    flag = 1
    while flag:
        
        for i in arr: 
            start -= i
            print(start)
            if start<lowerBound or start>upperBound:
                return total
                        
        start = low+1
        low += 1
        total += 1

        print("start:",start,"total:",total)
        
    return total   
   
arr = [-2,-1,-2,5]
print(countAnalogousArrays(arr, lowerBound=3,upperBound=10))