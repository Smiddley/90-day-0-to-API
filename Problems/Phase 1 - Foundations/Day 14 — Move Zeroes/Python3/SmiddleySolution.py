"""
Problem Statement

Given an array nums, move all 0s to the end while maintaining the relative order of non-zero elements.

Do this in-place.

Input

nums: array of integers

Output

Modified array (in-place)

Example
Input:  [0,1,0,3,12]
Output: [1,3,12,0,0]

Constraints

O(1) extra space

One pass preferred

Concept

Stable partitioning

Pointer-based compaction

Cloud Analogy

Filtering dropped packets while preserving order of valid traffic.

notes: 
Definitely need 2 pointers:
1 "fast" that is the current evaluation value location
1 "slow" that is the first zero location.

if nums[fast] is 0, set slow to fast
if nums[fast] is not 0, switch nums[fast] with nums[slow]

how to start?
find first 0 (everything before must therefore be non-zero)

"""

def move_zeros(nums: list[int])-> list[int]:
    if not nums:
        return[]

    zero_place = 0

    while zero_place < len(nums):
        if nums[zero_place] == 0:
            break
        zero_place +=1
    
    # print ("First zero index:",zero_place)
    for i in range(zero_place, len(nums)):
        # print (i)
        if nums[i] != 0:
            nums[zero_place] = nums[i]
            nums[i] = 0
            zero_place +=1
            # print(nums)

    return nums

if __name__=="__main__":
    tests= [
        [0,1,0,3,12], #[1,3,12,0,0]
        [], #[]
        [0,0,0,0,0,0], #[0,0,0,0,0,0]
        [1,1,2,2,3,4], #[1,1,2,2,3,4]
        [1,0,2,0,4], #[1,2,4,0,0]
    ]

    for test in tests:
        print(move_zeros(test))