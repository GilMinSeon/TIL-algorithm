class Solution(object):
    def maxProfit(self, prices):
        if len(prices) in (0,1):
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for target in prices:
            if target < min_price:
                min_price = target
            else:
                max_profit = max(max_profit, target - min_price)
        
        return max_profit

        # 실패한 풀이
        '''
        if len(prices) == 0 or len(prices) == 1: return 0

        res1, res2 = 0, 0

        low = min(prices)
        high = max(prices)

        idx_low = prices.index(low)
        idx_high = prices.index(high)

        if idx_high == 0 and idx_low == len(prices)-1:
            print('???')
            temp_list = prices[1:len(prices)-1]
            if len(temp_list) != 0:
                print(temp_list)
                low = min(temp_list)
                high = max(temp_list)

            idx_low = temp_list.index(low)
            idx_high = temp_list.index(high)

        case1 = prices[idx_low+1:]
        case2 = prices[:idx_high]

        if len(case1) != 0:
            res1 = max(case1) - low
        
        if len(case2) != 0:
            res2 = high - min(case2)

        return max(res1, res2)
        '''


        
