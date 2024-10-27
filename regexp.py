def is_match(text, pattern):

   
    # If text empty and pattern empty return true and if text not empty and pattern empty return false
    if not pattern:
        return not text
    
    # Check between text and pattern of the first characters if the match.
    first_match = bool(text) and pattern[0] in {text[0], '.'}

    # Check if the pattern has two characters and the first is asterisk
    # Condition True thus the asterisk and preceding character is zero.
    if len(pattern) >= 2 and pattern[1] == '*':

        # Case asterisk
        # Case 1 ignore the character and asterisk(zero) and continue 
        # Case 2 First match continue and remove the first character in the pattern
        return is_match(text, pattern[2:]) or (first_match and is_match(text[1:], pattern))
    else:
        return first_match and is_match(text[1:], pattern[1:]) # Checking the match between text and pattern in the first character, True continue
    
print(is_match("aab", "c*a*b"))  # Display the output