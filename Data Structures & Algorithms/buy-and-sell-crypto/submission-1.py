class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        sell_price = prices[0]
        max_profit = 0



        for index, price in enumerate(prices):
            print(index, price)
            if price > sell_price: # sell price is highest price 
                sell_price = price
                # print("Change sell_price")
            if price < buy_price:
                buy_price = price
                sell_price = price
                # print("Change buy_price")
            # print(sell_price)  
            # print(buy_price) 
            profit = sell_price - buy_price # calculate profit
            print(profit)
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

        # 0   0 new min 4 new max 5 new max 6 new max 1 ....   