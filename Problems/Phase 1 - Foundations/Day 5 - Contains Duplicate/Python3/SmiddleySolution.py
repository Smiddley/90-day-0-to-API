"""
Check if an array contains any duplicates.

Notes:

edge cases:
empty array -> false

Several ways to do this:
1) Compare length before and after transforming array into set
O(n) complexity, dominated by the transformation itsself (get len is O(1))
quick development time
can be extended to "which values are duplicates?"
loses order
cannot be generalized to "how many duplicate values?"

Pseudocode
has_duplicates(list) -> bool
if len(list) == len(set(list)) -> False #does not contain duplicates
else -> true

2) Dict of seen
worst case complexity is O(n), but return on first duplicate shortens runtime in practice
useful if array will be frequently searched downstream.
can be extended to both future cases mentioned about with small effort


3) counter of values
unclear complexity: generate counter dict is O(n), checking if any count is >1 either O(n) or O(1), need to read docs on built in dict function
depends on common Counter module; either must include module with deployment (airgapped envs) or add module to requirements.txt
easily extened into which and how many cases
"""
#Needed for Counter
import collections

#Not typing, to handle all hashable chars. Assuming all lists are hashable
def has_Duplicates(arr) -> bool:
    #empty list has no dupes
    if not arr:
        return False
    
    if len(arr) == len(set(arr)):
        return False

    return True

#Not typing, to handle all hashable chars. Assuming all lists are hashable
def has_Dupes_Dict(arr) -> bool:
    #empty list has no dupes
    if not arr:
        return False
    
    #reset dict to make function reusable
    seen = {}
    for char in arr:
        if char in seen:
            return True
        elif char not in seen:
            #add count logic to extend to "how many of each char"
            seen[char] = 1

    #if char never found in seen, no dupes. return False
    return False

#Not typing, to handle all hashable chars. Assuming all lists are hashable
def has_Dupes_Counter(arr) -> bool:
    #empty list has no dupes
    if not arr:
        return False
    
    count = collections.Counter(arr)
    
    #Probably can shorten with max val check
    for key in count:
        if count[key] > 1:
            return True
    
    return False

if __name__=="__main__":
    test = [[1,2,3,4,5,6,7],
            [1,1,2,3,4],
            ["a","b","c","d","e"],
            ["a","a","b"],
            []]
    
    for case in test:
        print("Set Algo:", has_Duplicates(case))
        print("Dict Algo:", has_Dupes_Dict(case))
        print("Counter Algo:", has_Dupes_Counter(case))
        print("")