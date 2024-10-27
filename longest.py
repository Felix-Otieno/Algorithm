def longest_substring(s):
    char_set = set()  # Use set to track unique characters in the substring
    start = 0        
    max_length = 0    
    
    for end in range(len(s)):  
        
        while s[end] in char_set:
            char_set.remove(s[start])  
            start += 1                 
        
        char_set.add(s[end])  
        max_length = max(max_length, end - start + 1) 

    return max_length

s = "xyzxyzyy"
print(longest_substring(s))
