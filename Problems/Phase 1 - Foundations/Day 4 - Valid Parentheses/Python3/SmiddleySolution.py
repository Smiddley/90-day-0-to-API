"""
Check if a string of parentheses is valid (open/close pairs match)

Notes:
Problem only calls for (), does not ask for {} or [] which would complicate the challenge
Since an ( must come before ), we can "count" by +1 for ( or -1 for ) and as long as count is never >0 and ends at 0, must be valid.
This ensures first character is (, last character is ), and that there are the same number of each.

O(n) average complexity, as we check every character. We reduce the actual runtime by returning False if counter < 0 without checking rest of string.

Edge case:
empty string -> True (as nothing matches nothing by default)
"""

def Check_Validity(string: str) -> bool:
    if not string:
        return True
    
    count = 0
    
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        
        if count < 0:
            return False
    
    if count != 0:
        return False
    
    return True

if __name__=="__main__":
    test_cases = ["()()()()()(())((()))",
                  ")(((())))(",
                  "",
                  "(((())))("]
    
    for i, case in enumerate(test_cases):
        print(f"Test Case {i+1}: {Check_Validity(case)}")