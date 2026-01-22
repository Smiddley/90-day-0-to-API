"""
Write a function that takes an array of integers and returns the sum of all numbers.

Example:

`Input: [1, 2, 3, 4, 5]
Output: 15

Input: []
Output: 0`


Constraints:

Array length: 0 ≤ n ≤ 1000

Integers can be positive, negative, or zero

Notes: 
Could do this with a for loop, adding each value to a total. This would be O(n)
Probably use some sort of math Sum() to get complexity to O(n), but higher clarity. This may not translate to Go as well.
"""
def addForLoop(arr: list[int]) -> int:
    total = 0
    for x in arr:
        total = total + x

    return total
    # print("For Loop Sum:",total)

def addViaSum(arr: list[int]) -> int:    
    return sum(arr)

if __name__=="__main__":
    arr = [1,2,3,4,5]
    total = addForLoop(arr)
    print(total)
    total = addViaSum(arr)
    print(total)