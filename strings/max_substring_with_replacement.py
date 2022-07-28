


def length_of_longest_substring(nums,k):

    window_start = 0
    numbers = {}
    max_len = 0
    
    for idx, number in enumerate(nums):
        
        if number not in numbers:
            numbers[number] = 1
            print(numbers)
            
        if number in numbers:
            numbers[number] += 1
            print(numbers)
        
        if 0 in numbers:
            zeros = numbers[0]
            if idx - window_start - zeros + 1 > k:
                numbers[nums[window_start]] -= 1
                window_start += 1
            
        max_len = max(max_len, idx - window_start +1)
        print("max_len",max_len)

    return max_len

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(length_of_longest_substring(nums,k))