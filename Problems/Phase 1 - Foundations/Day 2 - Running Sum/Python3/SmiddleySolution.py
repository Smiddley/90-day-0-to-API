# Given an array, return a new array where each element at index i is the sum of nums[0..i].

def sum_array(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return []
    
    ans = []
    total = 0

    for value in arr:
        total = total + value
        ans.append(total)
    
    return ans

if __name__ == "__main__":
    arr = [1,5,7,3,-7,8,3,4]
    print(sum_array(arr))