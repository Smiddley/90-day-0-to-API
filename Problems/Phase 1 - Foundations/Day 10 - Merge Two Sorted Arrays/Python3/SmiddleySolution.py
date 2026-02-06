"""
Problem Statement

Given two sorted arrays nums1 and nums2, return a new array containing all elements in sorted order.

Input

nums1: sorted array

nums2: sorted array

Output

A new sorted array

Example
Input:  [1,3,5], [2,4,6]
Output: [1,2,3,4,5,6]

Constraints

Do not re-sort the final array

Time complexity: O(n + m)

Concept

Two pointers

Linear merge

Cloud Analogy

Merging two sorted log streams by timestamp.


Notes:
new array, do not mutate inputs.
no re-sort means we must sort as we go
nested for loop is O(n^2) which is not acceptable
num1 and num2 are guarenteed sorted, no need to use dict (what would the O() be of dict solution?) (also would ignore targeted concepts (2 pointers and linear merge))


edge cases:
nums1,nums2 = [] -> ans = num2,nums1


"""

def combine_lists(nums1 : list[int], nums2: list[int])->list[int]:
    ans = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        # print("i=",i,"len(nums1)=", len(nums1),"j=",j,"len(nums2)=",len(nums2))
        if nums1[i] <= nums2[j]:
            ans.append(nums1[i])
            i +=1

        elif nums1[i] > nums2[j]:
            ans.append(nums2[j])
            j +=1

    while i < len(nums1):
        ans.append(nums1[i])
        i +=1

    while j < len(nums2):
        ans.append(nums2[j])
        j +=1
        
    return ans

if __name__=="__main__":
    tests = [
        [[],[]], # []
        [[1,3,5],[2,4,6]], #[1,2,3,4,5,6]
        [[],[2,4,6]], #[2,4,6]
        [[1,3,5],[]] #[1,3,5]
    ]

    for test in tests:
        print(test[0],"+",test[1], "=", combine_lists(test[0],test[1]))