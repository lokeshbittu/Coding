

def max_number_of_fruits(arr):
    
    fruits = {}
    window_start = 0
    max_fruits = 0

    for window_end in range(len(arr)):

        right_fruit = arr[window_end]

        if fruits[right_fruit] not in fruits:
            fruits[right_fruit] = 0
            print(fruits)

        fruits[right_fruit] += 1

        while(len(fruits)>2):
            left_fruit = arr[window_start]
            fruits[left_fruit] -= 1

            if fruits[left_fruit] == 0:
                fruits.pop(left_fruit)
            
            window_start += 1
        
        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits

Fruit=['A', 'B', 'C', 'A', 'C']
print(max_number_of_fruits(Fruit))