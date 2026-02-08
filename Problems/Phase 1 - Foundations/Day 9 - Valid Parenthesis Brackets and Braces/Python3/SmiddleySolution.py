"""
### Problem Statement

Given a string s containing only the characters ()[]{}, determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type
- Open brackets are closed in the correct order
- Every closing bracket has a corresponding open bracket

### Input

s: string

### Output

true or false

### Example
```
Input:  "()[]{}"
Output: true

Input:  "(]"
Output: false
```


Notes:
Feels like a data streaming problem
First element must be a "Left half", ( {  or [. Last element must be a "right half", ) } ]. 
Can have infinite left halfs, stream can only becomes invalid once a right half appears, or if end of string is reached with open left halfs.
Really the question is repeatedly asking "Does this right half complete the most recently seen left half?" If so, remove that left half from consideration.
This means we need a first in, last out structure; if I remember correctly thats a "stack" (Cause you add to and remove from the top of the stack)

Should be O(n) complexity (traverse string once, worst case store all chars of string in stack)
Pseudocode:

for char in string:
 if char == "{, [, or (" -> add to stack
 if char == "}, ], or )" then compare to most recent addition to stack.
    if matches -> pop stack.
    if not matches -> return False

At end of string, if any chars left in stack -> return false
else return true

"""

# #Correct but verbose
# def valid_braces(test: str)->bool:
#     stack = []
#     # print(test)

#     for char in list(test):
        
#         #add all open braces to stack
#         if char == "{" or char == "(" or char == "[":
#             stack.append(char)
        
#         else:
#             if len(stack) == 0:
#                 return False
            
#             if char == "}": 
#                 if stack[-1] == "{":
#                     stack.pop()
#                 else:
#                     return False    
            
#             elif char == ")":
#                 if stack[-1] == "(":
#                     stack.pop()
#                 else:
#                     return False
                
#             elif char == "]":
#                 if stack[-1] == "[":
#                     stack.pop()
#                 else:
#                     return False
            
        
#     if len(stack) == 0:
#         return True
#     else:
#         return False

def valid_braces(test: str) -> bool:
    stack = []
    pairs = {"(": ")", "{":"}","[":"]"}

    for char in test:
        if char in pairs:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if pairs[last] != char:
                return False
    
    return not stack
            

if __name__=="__main__":
    tests = [
        "()[]{}", #true
        "(]", #false
        "", #true
        "){}" #false
    ]
    for test in tests:
        print(test,"→",valid_braces(test))