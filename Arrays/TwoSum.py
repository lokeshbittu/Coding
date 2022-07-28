

def twosum(arr, target):

    hashmap = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        
        if diff in arr:
            
            return [arr[i], diff]
        
        hashmap[diff] = i
        print("hashmap", hashmap)

    return None

arr = [1,2,3,4,5]
target = 7

print("twosum", twosum(arr, target))