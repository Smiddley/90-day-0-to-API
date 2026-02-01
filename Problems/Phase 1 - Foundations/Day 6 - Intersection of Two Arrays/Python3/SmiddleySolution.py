"""
Return intersection of two arrays (unique elements only).

notes:
We are looking for listA AND listB, only unique elements that are in both lists
2 ways to do this are immediately apparent;

Edge cases:
- empty array -> []
- list a == list b -> list a&b (probably naturally)
- list a&b == [] -> [] (also naturally, worth testing)



Single pass:
Should be O(n**2) time complexity as have to traverse 2nd array for every value in array one. 
O(n) space complexity, since build as you go answer list
Useful if order needs to be preserved or if nonunique values needed


Set array & set array2
Should be O(n) time complexity, as conversion to set is O(n) for each array
Space complexity is O(n), but at least double the original (assuming converting to set takes up memory, will validate in docs later)


Fun third option: Can we use a lambda function here? Unsure of complexity. Not for prod until verify complexity

"""
#Not for prod
def intercept_lambda(arr, arr2) -> list:
    return list(filter(lambda x: x in arr,arr2))

def intercept_set(arr, arr2) -> list:
    return list(set(arr)&set(arr2))

def intercept_pass(arr, arr2) -> list:
    intercept = []
    
    #skipping dupes of arr 1 may speed up runtime, hence the dict
    seen = {}

    for x in arr:
        if x not in seen:
            seen[x] = 1
            if x in arr2:
                intercept.append(x)
    
    return intercept
if __name__=="__main__":
    test = [[1,2,3],
            [2,3],
            [2,3],
            [4,5],
            []]
    
    for i in range(len(test)-1):
        print("lambda:",intercept_lambda(test[i], test[i+1]))
        print("set:",intercept_set(test[i], test[i+1]))
        print("pass:", intercept_pass(test[i],test[i+1]))
        print()
