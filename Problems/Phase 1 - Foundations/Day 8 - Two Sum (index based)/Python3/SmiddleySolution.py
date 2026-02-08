"""Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

### You may assume:
Exactly one solution exists
You may not use the same element twice
Return the indices in any order.

### Input
nums: array of integers
target: integer

### Output
A pair of integers `[i, j]` such that `nums[i] + nums[j] == target`

### Constraints
```
2 ≤ len(nums) ≤ 10⁵
-10⁴ ≤ nums[i] ≤ 10⁴
```

### Example
```
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]
```

Notes:
We need to track indices and values. 
Order does not matter. 
perhaps converting array into dict with index as value is a good path? Lowers complexity significantly, as dict lookups are O(1)
The above assumptions are definitely pushing that way. 

Must handle empty list and no sol found explicitly. 
We only care about a solution, not ALL solutions. Therefore we can return first solution found.
Because of negative number inclusion, I dont see any math to limit search. (If positive ints only, can remove all vals greater than target)

Pseudocode:

make dict from array(array of ints) -> dict with num as key, and index as value
    for index, num in array
        if num not in dict already
            dict[num] = index
    return dict

find if compliment for num is in array

for num in array:
    if (target - num) in dict then return [dict[num], dict[target-num]]

This should be O(n) space as created a new dict
This should be O(n) time as both dict creation and array traversal are independant O(n)

Small optimization would be to traverse dict, as its guarenteed to be unique (same or fewer n)
but this optimization comes at the cost of development difficulty as it is much more natural to use values and not the keys themselves.
worth doing if best possible runtime is required (latentcy sensitive apps, data streaming)

"""

#Left for historical purposes, do not use for two_sums.
def list_to_dict(arr: list[int]) -> dict:
    index_dict = {}

    for index,val in enumerate(arr):
        if val not in index_dict:
            index_dict[val] = index

    return index_dict

#left for historical training purposes, do not use. Double element bug
def two_sum(nums: list[int], target: int) -> list[int]:
    
    if len(nums) < 2:
        return []
    
    index_dict = list_to_dict(nums)
    
    for val in nums:
        if target - val in index_dict:
            return [index_dict[val], index_dict[target-val]]
        
    return []

def two_sum_no_preload(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, num in enumerate(nums):
        if target - num in seen:
            return [seen[target-num], index]
        else:
            seen[num] = index

    #problem guarenteed answer, hence no return []

if __name__=="__main__":
    tests = [
        [[2,7,11,15], 9], # expect [0,1]
        [[-4,2,6,-2,9,4], 5], # expect [0,4]
    ]

    for test in tests:
        print("Test:",test[0],"\nTarget:",test[1], "\nIndices of solution:", two_sum_no_preload(test[0],test[1]),"\n")