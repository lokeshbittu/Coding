
from sympy import O


def longestSubstring(str):

    window_start = O
    s = ""
    max_length = 0

    for window_end in range(len(str)):
        
        if str[window_end] not in s:
            s += str[window_end]
        
        while(str[window_end] in s):
            s = s[window_start:]
            window_start += 1

            if window_start == window_end:
                s = ""
        
        max_length = max(max_length, window_end - window_start +1)

    return max_length

String="abccde"
print(longestSubstring(String))