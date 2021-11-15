# 买卖股票的最佳时机
store = 0  # 仓库最大只能是1
benifit = 0  # 获得的利益
temp_sale = 0  # 准备卖
temp_sale_prices = 0
prices = [7, 1, 6, 4, 3, 1, 9, 0]

for i in range(len(prices)):
    if store == 0 and temp_sale == 0:  # 如果仓库是空的 #只能是初次用哈
        buy_prices = prices[i]  # 当前入仓
        store = 1
    if i != len(prices) - 1:
        if store == 1 and temp_sale == 0:
            if prices[i] < buy_prices:
                buy_prices = prices[i]
            if prices[i] > buy_prices:
                temp_sale_prices = prices[i]
                temp_sale = 1
        if store == 1 and temp_sale == 1:
            if temp_sale_prices < prices[i]:
                temp_sale_prices = prices[i]
            if temp_sale_prices > prices[i]:
                benifit = benifit + temp_sale_prices - buy_prices  # 卖股票
                buy_prices = prices[i]
                temp_sale = 0
                temp_sale_prices = 0
    else:  # 如果到了数组的最后一项
        x = max(temp_sale_prices, prices[i])
        if x > buy_prices:
            benifit = benifit + x - buy_prices

print(benifit)
