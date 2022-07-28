

def Two_sum(nums):
    # n = len(nums)
        
    # first = 0
    # second = 1
    
    # while second < len(nums):
        
    #     print("First", first, "Second", second)
    #     if nums[first] == 0 and nums[second] != 0:
            
    #         nums[first], nums[second] = nums[second], nums[first]               
    #         first = first + 1
    #         print("nums", nums)
    #         print("first", first, "second", second)
            
    #     elif nums[first] != 0 or nums[second] != 0:
    #         first += 1
            
    #     second += 1
    
    # return nums
    index,c=0,0
		#index used for storing first zero index
		#c as a flag to not allow the index change for every zero
    for i in range(len(nums)):
        if nums[i]==0 and c==0: 
            index=i
            c=c+1
        else:
            #sort the element with first zero index which makes to push zeros back 
            if nums[i]!=0:
                nums[index],nums[i]=nums[i],nums[index]
                index=index+1
    print(nums)
    return nums

arr = [0,0,1, 0, 1]
print(Two_sum(arr))