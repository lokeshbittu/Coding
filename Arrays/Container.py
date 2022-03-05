
def maxArea( height):
    max_area = 0
    i = 0
    j = len(height)-1
    while i<j:
        diff = min(height[i],height[j])
        area = diff * (j-1)
        if (area > max_area):
            max_area = area
        
        print("i",i,"j",j,"area",area)

        if(height[i]>height[j]):
            j -= 1
            
        else:
            i += 1 
        
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
