"""
Problem Statement

Given an array prices where prices[i] is the price of a stock on day i, find the maximum profit you can achieve by choosing one day to buy and one later day to sell.
If no profit is possible, return 0.

Input
prices: array of integers

Output
Maximum profit (integer)

Example
Input:  [7,1,5,3,6,4]
Output: 5

Concept
Min-so-far tracking
Single-pass optimization

Cloud Analogy
Buy compute when cheap, sell reserved capacity when expensive.


Notes:
we need to track the profit, not the days that the purchase happened on
We know that buy day(i) is always smaller than sell day (s)
We check 2 things as we move through the array:

is the current price at prices[s] larger than or = to current buy day?
    if yes, calculate profit. 
        If current profit larger than max profit seen so far, 
            save current profit over max profit 
        then check the next day

    if no,
        move i to s, since all future prices in the list will not be more profitable
    
return max_profit

Constraints:
i<s; → 1 <= s <= len(prices)

Edge cases:
len(prices) < 2 -> return 0 as no profit possible (no day to sell)
if all future prices are smaller sequentially (prices[i] > prices[i+1] for all i) -> return 0 (no profit possible.)

assumptions:
all prices[i] are positive (no shorting the stock)

"""

def max_profit_single_transaction(prices: list[int]) -> int:
    i = max_profit = 0
    
    #current sell day
    s = 1

    while s < len(prices):
        if prices[s] > prices[i]:
            print("Buy date:",i,"| sell date:",s,"| Profit:", prices[s]-prices[i])
            max_profit= max(max_profit, prices[s]-prices[i])
            s += 1
        else:
            print("Move Buy day pointer to:",s)
            i=s
            s+=1

    return max_profit

def max_profit_correct(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    
    max_profit=0
    min_price = prices[0]

    for price in prices:
        if price > min_price:
            print("price:",price,"| min_price:",min_price,"| Profit:", price - min_price)
            max_profit= max(max_profit, price - min_price)
        else:
            print("move min_price to:",price)
            min_price = price

    return max_profit

if __name__=="__main__":

    tests = [
        [], # 0
        [3], # 0
        [7,1,5,3,6,4], #5
        [4,8,1,10], # 9
        [1,2,3,4,5], # 4
        [5,4,3,2,1] #0
    ]

    for test in tests:
        print("Test:", test, "Max Profit:", max_profit_single_transaction(test))
        print("Test:", test, "Max Profit:", max_profit_correct(test))