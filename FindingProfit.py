def maxprofit(price):
    n=len(price)
    maxp=0
    for i in range(1,n):
        if price[i]>price[i-1]:
            maxp+=price[i]-price[i-1]

    return maxp

n = int(input("Enter the number of days: "))

# Input the prices for each day
prices = list(map(int, input("Enter the prices: ").split()))

# Calculate and print the maximum profit
profit = maxprofit(prices)
print(profit)
