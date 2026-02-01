"""
Given an array of integers nums and a target integer target, return the indices of two numbers that add up to the target.

Example:

nums = [2,7,11,15], target = 9 → [0,1]
nums = [3,2,4], target = 6 → [1,2]


Cloud Analogy: Connection tracking table: hash map maps value → index.

Mental Notes:
List is unordered and indexes needed, so sorting is not useful. Not given any constraints, so array can be very long with large values.
we can "filter out" every number larger than X, which should cut run time down by 1/2

The immediate solution I see is:
for i in Enumerate(arr) < X
  if X - i in arr
    record index (x, x-i)

but this looks like O(N^2). How can we make this faster?
what if we make a second, sorted array? then we can binary search for pairs.
that'd probably get run time down to O(nlogn), while doubling the space used (still O(N))

we could convert to a hash map, preserving the indexes. Unclear how exactly that would help


A hashmap (Dictionary) should get complexity down to O(1) average, by checking for every i, has X-i been seen?
This means I do not (and should not) create a dict of the entire list, but rather build as we traverse the list
"""

def compliment_Calculator(arr: list[int], X: int) -> list[int]:
    ans = []

            # legacy code for interative learning, would not ship
            # #convert arr to dict
            # map = dict(enumerate(arr))

            # #find if compliment is in dict
            # for value in map.values:
            #     if X - value in map.values:
            #         ans.append()
            # return ans
            #this does not work as I need to retrieve the indexes, not the values themselves.
            #Also, problem only cares that any one solution works, no need for ALL solutions (could we extend?)

    # used to store value, index pair already checked
    seen={}

    # EDGE CASE: empty or short array input
    if len(arr) < 2:
        print("Not enough nums to compare")
        return ans
    
    for index, value in enumerate(arr):
        compliment = X - value
        if compliment in seen:
            ans.append(seen[compliment])
            ans.append(index)
            return ans
        
        seen[value] = index
    
    return ans


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(compliment_Calculator(nums, target))

    nums = [3,2,4]
    target = 6
    print(compliment_Calculator(nums, target))