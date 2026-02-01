"""
Find the maximum number of consecutive 1s in a binary array.

2 ways to do this:
convert array to string, split string on 0, get max of len()s
O(n) but development time is probably faster, and no state/pointer tracking
so less prone to error. Env permitting, use for more junior team or when
crashing a schedule to meet project deadline

edge cases:
empty array -> 0
value not 1 or 0 (unless input is prevalidated) -> raise exception *Not handling here, taking the assumption of guarenteed vals.
all 0's -> 0
all 1's -> len(input)

other way is single pass counter.
every value in list, 
if 1 add to counter, 
if 0 compare counter to max & save if larger & reset counter
return saved max
O(n) time, as traverses list once. O(1) space, as only saves a single int

Useful when memory is tightly constrained or streaming data constantly. 
More generic, easier to read for non-Py dev. Careful of off by 1 error from
not returning last segment

Edge Cases:
empty array -> 0
value not 1 or 0 (unless input is prevalidated) -> raise exception *Not handling here, taking the assumption of guarenteed vals.
all 0's -> 0
all 1's -> len(input)
off by one (last group of 1's not counted) -> max
"""

def max_single_pass(input: list[int]) -> int:
    #empty array edge case
    if len(input) == 0:
        return 0
    
    #Set internal to funct for reusability
    max_length = 0
    counter = 0
    for x in input:
        if x == 1:
            counter += 1
        else:
            if counter > max_length:
                max_length = counter
            counter = 0

    #Final segment check, handling off by one
    if counter > max_length:
        max_length = counter

    return max_length

def max_split_string(input: list[int]) -> int:
    #empty array edge case
    if len(input) == 0:
        return 0    

    #TODO Check if can combine into one line
    input_str = "".join(str(x) for x in input)
    input_str_list = input_str.split("0")

    return(max(len(x) for x in input_str_list))

if __name__=="__main__":
    #last subarray is longest to test for "off by one"
    input = [0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,1] #Expect 7 returned
    ans_single_pass = max_single_pass(input)
    
    ans_split_string = max_split_string(input)
    
    
    print("Single Pass algorhythm:", ans_single_pass, "\nSplit String algorhythm:", ans_split_string) 