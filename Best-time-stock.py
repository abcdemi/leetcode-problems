'''
Best time to buy and sell stock.
Given an array of prices, find best times to buy and sell the stock
'''

def maxProfit(prices):
    maximum, current = 0, 0
    for i in range(1, len(prices)):
        current = max(current + prices[i] - prices[i-1], 0)
        maximum = max(maximum, current)
    
    return maximum

print(maxProfit([7,1,5,3,6,4]))