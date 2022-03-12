


from turtle import left
from numpy import character


def longsubstring(s,distinct_number):
    
    window_start = 0
    character_frequency ={}
    max_length = 0

    for window_end in range(len(s)):
        
        if s[window_end] not in character_frequency:
            character_frequency[s[window_end]] = 0
        
        character_frequency[s[window_end]] += 1
        
        while(len(character_frequency)>distinct_number):
            left_character = s[window_start]
            character_frequency[left_character] -= 1
            if character_frequency[left_character] == 0:
                del character_frequency[left_character]
            window_start += 1
        
        
        max_length = max(max_length,window_end-window_start+1)
    
    return max_length

s = "araaci"
number = 2
print(longsubstring(s,number))