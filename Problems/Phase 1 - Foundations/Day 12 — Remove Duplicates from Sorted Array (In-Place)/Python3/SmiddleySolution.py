"""
Problem Statement

Given a sorted array nums, remove duplicates in-place such that each unique element appears once.

Return the number of unique elements k.

The first k elements of nums must contain the result.

Input

nums: sorted array

Output

Integer k

Example
Input:  [1,1,2]
Output: 2
Array after: [1,2,_]

Constraints

O(1) extra space

Order must be preserved

Concept

Fast/slow pointers

In-place mutation

Cloud Analogy

Deduplicating already-sorted telemetry streams.
"""
#note this does not keep the empty locations. Therefore this does not meet the constraints of the question
def sorted_set(nums:list[int]) -> int:
    return len(set(nums))

def pointer_sort(nums: list[int]) -> int:
    if not nums:
        return 0
    
    count = 0
    first_empty_pointer = 0
    
    for i, val in enumerate(nums):
        
        #set first element
        if i == 0: 
            last_unique = nums[i] 
            count +=1
            first_empty_pointer += 1

        else:
            if val == last_unique:

                if first_empty_pointer == 0: 
                    first_empty_pointer = i
                nums[i] = None
            
            else:
                count +=1
                last_unique = val
                nums[first_empty_pointer] = val 
                nums[i] = None 
                first_empty_pointer +=1

    return count


if __name__=="__main__":
    tests = [
        [],
        [1,1,1,1,1,1,1],
        [1,2,2,3,3,4,4,5,5,6,7]
    ]

    for test in tests:
        print("Test:", test, "Length:",len(test), "| Result:",sorted_set(test), "Length:",len(test))
        print("Test:", test, "Length:",len(test), "| Result:",pointer_sort(test), "Length:",len(test))